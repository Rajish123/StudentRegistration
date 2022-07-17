from student.models import Student
from django.contrib import messages
from student.forms import StudentForm
from django.shortcuts import render

def updateStudent(request, id):
    context = {}
    student = Student.get_student_by_id(id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Successfully")
    else:
        form = StudentForm(instance=student)
        context = {'form':form}
    return render(request,'student_form.html',context)