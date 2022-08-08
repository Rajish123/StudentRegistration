from django.http import HttpResponse,HttpResponseRedirect,Http404
from education.forms import EducationInfoForm
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect

from student.models import Student


def createEducationInfo(request,id):
    student = Student.get_student_by_id(id)
    if student:
        if request.method == "GET":
            form = EducationInfoForm(instance=student)
            return render(request,'education/educationinfo_create.html',{'form':form,'student':student})

        elif request.method == "POST":
            form = EducationInfoForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                messages.success(request,'Successfully created')
                return redirect('education:educationinfo_list')

            else:
                return HttpResponse("<h1>Form not valid</h1>")
        return render(request,'education/educationinfo_create.html',{'form':form,'student':student})
    else:
        raise Http404()

