from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


# Create your views here.
class PhotoAddPageView(CreateView):
    pass


class PhotoDetailsView(DetailView):
    pass


class PhotoEditPageView(UpdateView):
    pass


class PhotoDeletePageView(DeleteView):
    pass