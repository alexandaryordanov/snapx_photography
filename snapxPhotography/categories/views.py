from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


# Create your views here.
class CategoryDashboardView(ListView):
    pass


class CategoryAddPageView(CreateView):
    pass


class CategoryEditPageView(UpdateView):
    pass


class CategoryDetailsView(DetailView):
    pass


class CategoryDeleteView(DeleteView):
    pass