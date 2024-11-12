from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


# Create your views here.
class AccountLoginView(LoginView):
    pass


class AccountRegisterView(CreateView):
    pass


class AccountDetailView(DetailView):
    pass


class AccountEditView(UpdateView):
    pass


class AccountDeleteView(DeleteView):
    pass