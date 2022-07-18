from batch.models import Batch
from django import forms

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'exampleInputBatchName'})
        }

