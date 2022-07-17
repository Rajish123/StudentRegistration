from operator import imod
from django.urls import path

from student.views import student_detail
from .views import create_student,update_student

app_name = 'student'

urlpatterns = [
    # path('',create_student.CreateStudent.as_view())
    # path('',create_student.AddView.as_view())
    path('create_student',create_student.create_student, name = 'create_student'),
    path('update_student/<str:id>',update_student.updateStudent, name = 'update_student'),
    path('detail_student/<str:id>',student_detail.studentDetail, name = 'detail_student'),


]
