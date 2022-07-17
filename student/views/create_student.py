from django.shortcuts import render
from django.contrib import messages
from student.models import *

from student.forms import StudentForm

def create_student(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request,'student_form.html',{'form':form})
    elif request.method == "POST":
        print(list(request.POST.items()))
        form = StudentForm(request.POST)
        if form.is_valid():
            print("valid")
            name = form.cleaned_data.get('name')
            print(name)
            form.save()
            messages.success(request,f"Account for {name} successfully created.")
            # return redirect('store:index')
        return render(request,'student_form.html',{'form':form})