from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from snapxPhotography.common.forms import SearchForm
from snapxPhotography.contests.forms import ContestAddForm, ContestDeleteForm
from snapxPhotography.contests.models import Contest


class ContestsDashboardView(ListView):
    model = Contest
    template_name = 'contests/dashboard_contest.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['search_form'] = SearchForm(self.request.GET)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        contest_name = self.request.GET.get('contest_name')
        category = self.request.GET.get('category')
        award = self.request.GET.get('award')

        if award == 'first':
            start = 1000
            end = 1499
        elif award == 'second':
            start = 1500
            end = 2499
        elif award == 'third':
            start = 2500
            end = 3499
        elif award == 'last':
            start = 3500
            end = 9999
        else:
            start = 1000
            end = 9999

        if contest_name and category:
            queryset = queryset.filter(name__icontains=contest_name, category__pk=category,
                                       award__gte=start, award__lte=end)
        elif contest_name:
            queryset = queryset.filter(name__icontains=contest_name, award__gte=start, award__lte=end)
        elif category:
            queryset = queryset.filter(category__pk=category, award__gte=start, award__lte=end)
        elif award:
            queryset = queryset.filter(award__gte=start, award__lte=end)

        return queryset


class ContestAddPageView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Contest
    form_class = ContestAddForm
    template_name = 'contests/add_contest.html'
    success_url = reverse_lazy('contest-dashboard')

    def form_valid(self, form):
        contest = form.save(commit=False)
        contest.created_by = self.request.user

        return super().form_valid(form)

    def test_func(self):
        return not self.request.user.is_staff

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)

class ContestDetailsView(LoginRequiredMixin, DetailView):
    model = Contest
    template_name = 'contests/details_contest.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        photos_list = self.object.photo.all()
        if photos_list:
            paginator = Paginator(photos_list, 12)
            page_number = self.request.GET.get('page')
            photos = paginator.get_page(page_number)
            contex['photos'] = photos

        return contex


class ContestDeletePageView(UserPassesTestMixin, DeleteView):
    model = Contest
    template_name = 'contests/delete_contest.html'
    form_class = ContestDeleteForm
    success_url = reverse_lazy('contest-dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def test_func(self):
        contest = get_object_or_404(Contest, pk=self.kwargs['pk'])
        return self.request.user == contest.created_by

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)