from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from snapxPhotography.accounts.forms import MyAppUserCreationForm, AccountEditForm
from snapxPhotography.accounts.models import Account

# Create your views here.

UserModel = get_user_model()


class AccountLoginView(LoginView):
    template_name = 'accounts/login_page.html'

    def form_valid(self, form):
        remember_me = self.request.POST.get("remember")

        if remember_me:
            self.request.session.set_expiry(30 * 24 * 60 * 60)
        else:
            self.request.session.set_expiry(24*60*60)

        return super().form_valid(form)


class AccountRegisterView(CreateView):
    model = UserModel
    form_class = MyAppUserCreationForm
    template_name = 'accounts/register_page.html'
    success_url = reverse_lazy('login')


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'accounts/account_details.html'


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
