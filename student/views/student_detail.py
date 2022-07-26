from django.http import Http404
from django.shortcuts import render
from student.models import Student
from django.http import Http404

def studentDetail(request,id):
    context = {}
    student = Student.get_student_by_id(id)
    if student:
        context['student'] = student
        return render(request, 'student/student_detail.html',context)
    else:
        raise Http404()