from college.models import CollegeInformation
from django.shortcuts import render

def listCollegeInfo(request):
    collegeinfo = CollegeInformation.get_all_collegeinfo()
    return render(request,'college/collegeinfo_list.html',{'college_info':collegeinfo})