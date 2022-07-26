from django.urls import path
from family.views import familyinfo_create,familyinfo_list,familyinfo_detail,familyinfo_update

app_name = 'family'

urlpatterns = [
    # requires student id
    path('familyinfo_create/<str:id>',familyinfo_create.createFamilyInfo, name = 'familyinfo_create'),
    path('familyinfo_list',familyinfo_list.listFamilyInfo, name = 'familyinfo_list'),
    path('familyinfo_detail/<str:id>',familyinfo_detail.familyinfoDetail, name = 'familyinfo_detail'),
    path('familyinfo_update/<str:id>',familyinfo_update.updateFamilyInfo, name = 'familyinfo_update')

]
