from django.shortcuts import render
from student.models import Student
from student.forms import StudentForm

def studentDetail(request,id):
    context = {}
    student = Student.get_student_by_id(id)
    context['student'] = student
    return render(request, 'student_detail.html',context)