from dataclasses import field
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'exampleInputName'}),
            'email': forms.TextInput(attrs={'class':'form-control','id':'exampleInputEmail'}),
            'mobile': forms.TextInput(attrs={'class':'form-control','id':'exampleInputMobile'}),
            'citizenship': forms.TextInput(attrs={'class':'form-control','id':'exampleInputMobile'}),
            'gender': forms.TextInput(attrs={'class':'form-control','id':'exampleInputGender'}),
            'blood_group': forms.TextInput(attrs={'class':'form-control','id':'exampleInputBloodGroup'}),
            'temp_address': forms.TextInput(attrs={'class':'form-control','id':'exampleInputTempAddress'}),
            'perm_address': forms.TextInput(attrs={'class':'form-control','id':'exampleInputPermanentAddress'}),
            'dob':forms.TextInput(attrs = {'class':'form-control','id':'exampleInputDob'}),
            'is_active': forms.CheckboxInput(attrs = {'class':'form-control', 'id':'exampleInputIsactive'}),
            'is_alumi': forms.CheckboxInput(attrs = {'class':'form-control', 'id':'exampleInputIsalumi'}),
            'picture': forms.FileInput(attrs = {'class':'form-control', 'id':'exampleInputFile'}),

        }


        # widgets = {
        #     # 'student': forms.HiddenInput(attrs={'class':'form-control','id':'exampleInputStudent', 'value' : {{student}}}),
        #     'symbol': forms.TextInput(attrs={'class':'form-control','id':'exampleInputSymbol'}),
        #     'board': forms.TextInput(attrs={'class':'form-control','id':'exampleInputBoard'}),
        #     'institution_name': forms.TextInput(attrs={'class':'form-control','id':'exampleInputInstitution'}),
        #     'cgpa': forms.TextInput(attrs={'class':'form-control','id':'exampleInputCgpa'}),
        #     'passed_year': forms.TextInput(attrs={'class':'form-control','id':'exampleInputPassedYear'})
        # }
    