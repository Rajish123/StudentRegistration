from operator import imod
from django.urls import path

from student.views import create_student, homeview,update_student,student_detail,student_list,homeview,delete_student
app_name = 'student'

urlpatterns = [
    path('',homeview.Home, name = 'home'),
    path('create_student',create_student.create_student, name = 'create_student'),
    path('update_student/<str:id>',update_student.updateStudent, name = 'update_student'),
    path('detail_student/<str:id>',student_detail.studentDetail, name = 'detail_student'),
    path('student_list',student_list.studentList, name = 'student_list'),
    path('delete_student/<str:id>',delete_student.deleteStudent,name = 'delete_student'),



 
]
