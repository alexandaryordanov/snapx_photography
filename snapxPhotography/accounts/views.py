from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from snapxPhotography.accounts.forms import MyAppUserCreationForm, AccountEditForm
from snapxPhotography.accounts.models import Account
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
        contex = super().get_context_data(**kwargs)
        photos_list = self.object.user.photos.all()
        if photos_list:
            paginator = Paginator(photos_list, 12)
            page_number = self.request.GET.get('page')
            photos = paginator.get_page(page_number)
            contex['photos'] = photos
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
        contex['total_earned'] = total_earned
        contex['contest_won'] = contest_won
        contex['total_contests'] = Contest.objects.count()
        contex['total_photos'] = Photo.objects.count()
        contex['total_closed'] = len(closed_contests)
        return contex

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user.is_staff and not self.request.user.is_staff:
            raise PermissionDenied("You are not allowed to view this page.")

        return obj


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
