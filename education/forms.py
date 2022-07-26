from education.models import EducationInformation
from django import forms


class EducationInfoForm(forms.ModelForm):

    class Meta:
        model = EducationInformation
        fields = "__all__"