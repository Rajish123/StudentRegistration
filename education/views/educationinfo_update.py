from django.http import HttpResponseRedirect, Http404
from student.models import Student
from education.models import EducationInformation

from education.forms import EducationInfoForm
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse

def updateEducationInfo(request,id):
    context = {}
    educationinfo = EducationInformation.get_educationinfo_by_id(id)
    student = educationinfo.student
    if educationinfo:
        initial_dict = {
            'student':student.id,
            'symbol_number':educationinfo.symbol_number,
            'board':educationinfo.board,
            'institution_name':educationinfo.institution_name,
            'cgpa':educationinfo.cgpa,
            'passed_year':educationinfo.passed_year
        }
        if request.method == "POST":
            form = EducationInfoForm(request.POST,instance=educationinfo)
            if form.is_valid():
                form.save()
                messages.success(request,'Updated Successfully')
                return HttpResponseRedirect(reverse('education:educationinfo_detail', args = [educationinfo.id]))

        else:
            form = EducationInfoForm(initial = initial_dict)
        context = {'form':form, 'student':student}

        return render(request,'education/educationinfo_update.html',context)
        

    else:
        raise Http404()