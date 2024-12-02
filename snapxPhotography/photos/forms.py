from django import forms

from snapxPhotography.photos.models import Photo


class PhotoBaseFrom(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['uploaded_by']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image.name.lower().endswith('.jpg'):
            raise forms.ValidationError('Only .jpg files are allowed')
        return image

    def clean_contest(self):
        contest = self.cleaned_data.get('contest')
        if contest and not contest.is_open:
            raise forms.ValidationError('Contest must be open. Please do not try to trick the application')
        return contest


class PhotoAddForm(PhotoBaseFrom):
    pass


class PhotoDeleteForm(PhotoBaseFrom):
    pass
