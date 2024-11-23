from django import forms

from snapxPhotography.categories.models import Category


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['created_by']


class CategoryAddForm(CategoryBaseForm):
    pass


class CategoryEditForm(CategoryBaseForm):
    pass
