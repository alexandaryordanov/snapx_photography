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


class ContactForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name...'
    }))

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email...'
    }))

    telephone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Telephone...'
    }))

    subject = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject...'
    }))

    message = forms.CharField(
        widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message...'
    }))
