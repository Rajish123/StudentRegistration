from student.models import Student
from django.contrib import messages
from student.forms import StudentForm
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404

def updateStudent(request, id):
    context = {}
    student = Student.get_student_by_id(id)
    if student:
        if request.method == "POST":
            form = StudentForm(request.POST, instance = student)
            if form.is_valid():
                form.save()
                messages.success(request,"Updated Successfully")
                return HttpResponseRedirect(reverse('student:detail_student', args = [student.id]))
        else:
            form = StudentForm(instance=student)
            context = {'form':form}
        return render(request,'student/student_form.html',context)
    else:
        raise Http404()