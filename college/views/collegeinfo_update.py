from http.client import HTTPResponse
from college.models import CollegeInformation
from django.http import Http404
from django.shortcuts import render
from college.forms import CollegeInfoForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse




def updateCollegeInfo(request,id):
    context = {}
    collegeinfo = CollegeInformation.get_collegeinfo_by_id(id)
    if collegeinfo:
        student = collegeinfo.student
        batch = collegeinfo.batch
        semester = collegeinfo.semester
        faculty = collegeinfo.faculty
        initial_dict = {
            'student':student.id,
            'batch':batch.id,
            'semester':semester.id,
            'faculty':faculty.id,
            'tu_registration_number':collegeinfo.tu_registration_number,
            'symbol_number':collegeinfo.symbol_number

        }
        if request.method == "POST":
            form = CollegeInfoForm(request.POST, instance = collegeinfo)
            if form.is_valid():
                form.save()
                messages.success(request,'Updated Successfully')
                return HttpResponseRedirect(reverse('college_info:collegeinfo_detail', args = [collegeinfo.id]))
                return HttpResponse("<h1>UPDATE SUCCESSFUL</h1>")
        else:
            form = CollegeInfoForm(initial = initial_dict)
            context = {'student':student,'batches':batch,'semesters':semester,'facultys':faculty} 
            return render(request,'college/collegeinfo_update.html',context)
    else:
        raise Http404()