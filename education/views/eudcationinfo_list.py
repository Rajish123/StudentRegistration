from student.models import Student
from education.models import EducationInformation

from django.shortcuts import render

def listEducationInfo(request):
    students = Student.get_all_student()
    educationinfo = EducationInformation.get_all_educationinfo()
    return render(request,'education/educationinfo_list.html',{'students':students,'education_info':educationinfo})
