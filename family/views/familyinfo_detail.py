from django.shortcuts import render
from family.models import FamilyInformation
from django.http import Http404

def familyinfoDetail(request,id):
    context = {}
    familyinfo = FamilyInformation.get_familyinfo_by_id(id)
    if familyinfo:
        context['familyinfo'] = familyinfo
        return render(request,'family/familyinfo_detail.html',context)
    else:
        raise Http404()