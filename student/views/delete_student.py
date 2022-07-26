from django.http import HttpResponse
from django.shortcuts import redirect
from student.models import Student
from django.shortcuts import redirect, render
from django.http import Http404

def deleteStudent(request,id):
    context = {}
    student = Student.get_student_by_id(id)
    if student:
        if request.method == "POST":
            student.delete()
            return redirect('student:student_list')
        return render(request,'student/student_delete.html')
    else:
        raise Http404()