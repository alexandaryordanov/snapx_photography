from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from snapxPhotography.categories.forms import CategoryAddForm, CategoryEditForm
from snapxPhotography.categories.models import Category


# Create your views here.
class CategoryDashboardView(ListView):
    model = Category
    template_name = 'categories/dashboard_category.html'
    paginate_by = 4


class CategoryAddPageView(UserPassesTestMixin, CreateView):
    model = Category
    form_class = CategoryAddForm
    template_name = 'categories/add_category.html'
    success_url = reverse_lazy('category-dashboard')

    def form_valid(self, form):
        category = form.save(commit=False)
        category.created_by = self.request.user

        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff


class CategoryEditPageView(UserPassesTestMixin, UpdateView):
    model = Category
    template_name = 'categories/edit_category.html'
    success_url = reverse_lazy('category-dashboard')
    form_class = CategoryEditForm

    def test_func(self):
        return self.request.user.is_staff


class CategoryDeleteView(UserPassesTestMixin, DeleteView):
    model = Category
    template_name = "categories/delete_category.html"
    success_url = reverse_lazy('category-dashboard')

    def test_func(self):
        return self.request.user.is_staff
