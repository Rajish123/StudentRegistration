from student.models import Student
from django.shortcuts import render


def studentList(request):
    context = {}
    student_list = Student.get_all_student()
    context ={'students':student_list} 
    return render(request, 'student/student_list.html', context)
