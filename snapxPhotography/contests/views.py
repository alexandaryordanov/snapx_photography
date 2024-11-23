from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from snapxPhotography.contests.forms import ContestAddForm
from snapxPhotography.contests.models import Contest


class ContestsDashboardView(ListView):
    model = Contest
    template_name = 'contests/dashboard_contest.html'


class ContestAddPageView(CreateView):
    model = Contest
    form_class = ContestAddForm
    template_name = 'contests/add_contest.html'
    success_url = reverse_lazy('contest-dashboard')

    def form_valid(self, form):
        contest = form.save(commit=False)
        contest.created_by = self.request.user

        return super().form_valid(form)


class ContestDetailsView(DetailView):
    model = Contest
    template_name = 'contests/details_contest.html'


class ContestEditPageView(UpdateView):
    pass


class ContestDeletePageView(DeleteView):
    pass
