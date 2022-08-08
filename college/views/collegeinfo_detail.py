
from multiprocessing import context
from django.shortcuts import render
from college.models import CollegeInformation
from django.http import Http404


def collegeInfoDetail(request,id):
    context = {}
    collegeinfo = CollegeInformation.get_collegeinfo_by_id(id)
    if collegeinfo:
        context = {'collegeinfo':collegeinfo}
        return render(request,'college/collegeinfo_detail.html',context)