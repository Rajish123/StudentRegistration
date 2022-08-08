from django.http import HttpResponse
from django.shortcuts import redirect
from education.models import EducationInformation

from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages

def deleteEducationInfo(request,id):
    educationinfo = EducationInformation.get_educationinfo_by_id(id)
    if educationinfo:
        if request.method == "POST":
            educationinfo.delete()
            messages.success(request,"Information deleted successfully")
            return redirect('education:educationinfo_list')
        return render(request,'education/educationinfo_delete.html')
    else:
        raise Http404()