from django.shortcuts import render
from education.models import EducationInformation
from django.http import Http404

def educationinfoDetail(request,id):
    context = {}
    educationinfo = EducationInformation.get_educationinfo_by_id(id)
    if educationinfo:
        context['educationinfo'] = educationinfo
        return render(request,'education/educationinfo_detail.html',context)
    else:
        raise Http404()