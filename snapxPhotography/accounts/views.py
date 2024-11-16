from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from snapxPhotography.accounts.forms import MyAppUserCreationForm, AccountEditForm
from snapxPhotography.accounts.models import Account

# Create your views here.

UserModel = get_user_model()


class AccountLoginView(LoginView):
    template_name = 'accounts/login_page.html'


class AccountRegisterView(CreateView):
    model = UserModel
    form_class = MyAppUserCreationForm
    template_name = 'accounts/register_page.html'
    success_url = 'login'


class AccountDetailView(DetailView):
    model = Account
    template_name = 'accounts/account-details.html'


class AccountEditView(UpdateView):
    model = Account
    form_class = AccountEditForm
    template_name = 'accounts/account_edit_page.html'

    def get_success_url(self):
        return reverse_lazy(
            'account-details',
            kwargs={'pk': self.object.pk}
        )


class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'accounts/account_delete_page.html'
    success_url = reverse_lazy('index')
