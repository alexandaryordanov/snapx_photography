from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


class ContestsDashboardView(ListView):
    pass


class ContestAddPageView(CreateView):
    pass


class ContestDetailsView(DetailView):
    pass


class ContestEditPageView(UpdateView):
    pass


class ContestDeletePageView(DeleteView):
    pass
