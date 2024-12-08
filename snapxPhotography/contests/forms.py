from django import forms
from snapxPhotography.contests.models import Contest
from snapxPhotography.mixins import DisabledFieldsMixin


class ContestBaseForm(forms.ModelForm):
    class Meta:
        model = Contest
        exclude = ['created_by']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }


class ContestAddForm(ContestBaseForm):
    pass


class ContestDeleteForm(DisabledFieldsMixin, ContestBaseForm):
    disabled_fields = ['name', 'requirements', 'award', 'deadline']

    class Meta(ContestBaseForm.Meta):
        exclude = ['category', 'created_by']
