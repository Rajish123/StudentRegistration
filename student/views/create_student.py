from django.shortcuts import render, redirect
from django.contrib import messages
from student.models import *

from student.forms import StudentForm

def create_student(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request,'student/student_form.html',{'form':form})
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            form.save()
            messages.success(request,f"Account for {name} successfully created.")
            return redirect('family:family_list')
        return render(request,'student/student_form.html',{'form':form})