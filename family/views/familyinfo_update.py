from django.http import HttpResponseRedirect, Http404
from family.models import FamilyInformation

from family.forms import FamilyInfoForm
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse

def updateFamilyInfo(request,id):
    context = {}
    familyinfo = FamilyInformation.get_familyinfo_by_id(id)
    student = familyinfo.student
    if familyinfo:
        initial_dict = {
            'student':student.id,
            'fathers_name':familyinfo.fathers_name,
            'mothers_name':familyinfo.mothers_name,
            'fathers_number':familyinfo.fathers_number,
            'mothers_number':familyinfo.mothers_number,
            'guardian_name':familyinfo.guardian_name,
            'guardian_relation':familyinfo.guardian_relation

        }
        print(initial_dict)
        if request.method == "POST":
            form = FamilyInfoForm(request.POST,instance=familyinfo,initial = initial_dict)
            if form.is_valid():
                form.save()
                messages.success(request,'Updated Successfully')
                return HttpResponseRedirect(reverse('family:familyinfo_detail', args = [familyinfo.id]))

        else:
            form = FamilyInfoForm(initial = initial_dict)
        context = {'form':form, 'student':student}

        return render(request,'family/familyinfo_update.html',context)
        

    else:
        raise Http404()