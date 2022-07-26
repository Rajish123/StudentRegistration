from django import forms
from family.models import FamilyInformation

class FamilyInfoForm(forms.ModelForm):
    class Meta:
        model = FamilyInformation
        fields = "__all__"