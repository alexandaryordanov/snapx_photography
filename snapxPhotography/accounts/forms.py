from cloudinary import CloudinaryResource
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.timezone import now
from snapxPhotography.accounts.models import Account

UserModel = get_user_model()


class MyAppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class MyAppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom labels
        self.fields['username'].label = "Your Username :"
        self.fields['email'].label = "Your Email Address :"
        self.fields['password1'].label = "Password :"
        self.fields['password2'].label = "Repeat Password :"


class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ['user']
        widgets = {
            'date_of_birth': forms.SelectDateWidget(years=range(1800, now().year + 1)),
        }

    def clean_profile_picture(self):
        image = self.cleaned_data.get('profile_picture')
        if isinstance(image, CloudinaryResource):
            return image
        if image and not image.name.lower().endswith('.jpg'):
            raise forms.ValidationError('Only .jpg files are allowed')
        return image
