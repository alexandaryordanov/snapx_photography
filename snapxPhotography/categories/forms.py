from django import forms
from snapxPhotography.categories.models import Category


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['created_by']

    def clean_category_image(self):
        image = self.cleaned_data.get('category_image')
        if image and not image.name.lower().endswith('.png'):
            raise forms.ValidationError('Only .png files are allowed')
        return image


class CategoryAddForm(CategoryBaseForm):
    pass


class CategoryEditForm(CategoryBaseForm):
    pass
