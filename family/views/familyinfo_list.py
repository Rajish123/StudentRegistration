from student.models import Student
from family.models import FamilyInformation
from django.shortcuts import render

def listFamilyInfo(request):
    students = Student.get_all_student()
    familyinfo = FamilyInformation.get_all_familyinfo()
    return render(request,'family/familyinfo_list.html',{'students':students,'family_info':familyinfo})
