from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from rest_framework import status

from snapxPhotography.accounts.forms import MyAppUserCreationForm, AccountEditForm
from snapxPhotography.accounts.models import Account
from snapxPhotography.common.forms import ContactForm
from snapxPhotography.common.utils import EmailThread
from snapxPhotography.contests.models import Contest
from snapxPhotography.photos.models import Photo

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


class AccountRegisterView(CreateView):
    model = UserModel
    form_class = MyAppUserCreationForm
    template_name = 'accounts/register_page.html'
    success_url = reverse_lazy('login')


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
        closed_contests = Contest.objects.filter(deadline__lt=timezone.now().date())
        contest_winners = []
        total_earned = 0
        contest_won = 0
        for contest in closed_contests:
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

            # Asynchronous email sending
            email_subject = f"{subject}"
            email_body = f"User with email:{sender_email} and tel: {phone} sends you this Message: \n\n {message}"
            from_email = 'anonimovbg@gmail.com'
            recipient_list = [f'{self.get_object().user.email}']

            EmailThread(email_subject, email_body, from_email, recipient_list).start()

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


class AccountDeleteView(UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/account_delete_page.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        account = get_object_or_404(Account, pk=self.kwargs['pk'])
        return self.request.user == account.user
