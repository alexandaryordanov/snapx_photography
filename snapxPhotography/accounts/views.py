from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from rest_framework import status
from snapxPhotography.accounts.forms import MyAppUserCreationForm, AccountEditForm
from snapxPhotography.accounts.models import Account
from snapxPhotography.common.forms import ContactForm
from snapxPhotography.common.utils import send_email_async
from snapxPhotography.contests.models import Contest
from snapxPhotography.photos.models import Photo
import asyncio

# Create your views here.

UserModel = get_user_model()


class AccountLoginView(LoginView):
    template_name = 'accounts/login_page.html'

    def form_valid(self, form):
        remember_me = self.request.POST.get("remember")

        if remember_me:
            self.request.session.set_expiry(30 * 24 * 60 * 60)
        else:
            self.request.session.set_expiry(24 * 60 * 60)

        return super().form_valid(form)

    @method_decorator(user_passes_test(lambda user: not user.is_authenticated, login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AccountRegisterView(CreateView):
    model = UserModel
    form_class = MyAppUserCreationForm
    template_name = 'accounts/register_page.html'
    success_url = reverse_lazy('login')

    @method_decorator(user_passes_test(lambda user: not user.is_authenticated, login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'accounts/account_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos_list = self.object.user.photos.all()
        if photos_list:
            paginator = Paginator(photos_list, 12)
            page_number = self.request.GET.get('page')
            photos = paginator.get_page(page_number)
            context['photos'] = photos
        closed_contests = Contest.objects.filter(deadline__lte=timezone.now().date())
        contest_winners = []
        total_earned = 0
        contest_won = 0
        for contest in closed_contests:
            if contest.photo.first():
                contest_winners.append(contest.photo.first())
        for photo in photos_list:
            if photo in contest_winners:
                total_earned += photo.contest.award
                contest_won += 1
        context['total_earned'] = total_earned
        context['contest_won'] = contest_won
        context['total_contests'] = Contest.objects.count()
        context['total_photos'] = Photo.objects.count()
        context['total_closed'] = len(closed_contests)
        context['form'] = ContactForm()
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user.is_staff and not self.request.user.is_staff:
            raise PermissionDenied("You are not allowed to view this page.")

        return obj

    def post(self, request, *args, **kwargs):

        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender_email = form.cleaned_data['email']
            phone = form.cleaned_data['telephone']

            email_subject = f"{subject}"
            email_body = f"User with email:{sender_email} and tel: {phone} sends you this Message: \n\n {message}"
            recipient_list = [f'{self.get_object().user.email}']

            asyncio.run(send_email_async(
                subject=email_subject,
                message=email_body,
                recipient_list=recipient_list,
            ))

            return JsonResponse({'message': 'Your message has been sent successfully!'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)


class AccountEditView(UserPassesTestMixin, UpdateView):
    model = Account
    form_class = AccountEditForm
    template_name = 'accounts/account_edit_page.html'

    def get_success_url(self):
        return reverse_lazy(
            'account-details',
            kwargs={'pk': self.object.pk}
        )

    def test_func(self):
        account = get_object_or_404(Account, pk=self.kwargs['pk'])
        return self.request.user == account.user

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)


class AccountDeleteView(UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/account_delete_page.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        account = get_object_or_404(Account, pk=self.kwargs['pk'])
        return self.request.user == account.user

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)
