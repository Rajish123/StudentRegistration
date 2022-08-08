from college.models import CollegeInformation
from django import forms

class CollegeInfoForm(forms.ModelForm):
    class Meta:
        model = CollegeInformation
        fields = "__all__"