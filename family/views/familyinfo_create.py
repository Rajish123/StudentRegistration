from django.http import Http404
from student.models import Student
from family.forms import FamilyInfoForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import Http404


def createFamilyInfo(request,id):
    student = Student.get_student_by_id(id)
    if student:
        if request.method == "POST":
            form = FamilyInfoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Successfully Created')
                return redirect('family:familyinfo_list')
        else:
            form =FamilyInfoForm(instance=student)

        return render(request,'family/familyinfo_create.html',{'form':form,'student':student})
    else:
        return Http404()