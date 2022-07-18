from django.shortcuts import redirect
from student.models import Student
from django.shortcuts import redirect, render

def deleteStudent(request,id):
    context = {}
    student = Student.get_student_by_id(id)
    if request.method == "POST":
        student.delete()
        return redirect('student:student_list')
    return render(request,'delete_student.html')