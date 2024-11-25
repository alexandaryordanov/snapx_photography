from django import forms

from snapxPhotography.categories.models import Category


class SearchForm(forms.Form):
    AwardChoices = [
        ('zero', 'All prices'),
        ('first', '$1,000 to $1,499'),
        ('second', '$1,500 to $2,499'),
        ('third', '$2,500 to $3,499'),
        ('last', '$3,500+')
    ]

    contest_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter contest name...',
            }
        )
    )

    category = forms.ModelChoiceField(
        required=False,
        queryset=Category.objects.all(),
        empty_label="Select a Category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    award = forms.ChoiceField(
        choices=AwardChoices,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
