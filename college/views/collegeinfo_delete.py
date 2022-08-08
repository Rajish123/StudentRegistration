from college.models import CollegeInformation
from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect,render


def deleteCollegeInfo(request,id):
    collegeinfo = CollegeInformation.get_collegeinfo_by_id(id)
    if collegeinfo:
        if request.method == "POST":
            collegeinfo.delete()
            messages.success(request,"Information deleted successfully")
            return redirect('college_info:collegeinfo_list')
        return render(request,'college/collegeinfo_delete.html')
    else:
        raise Http404()