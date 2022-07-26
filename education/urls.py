from django.urls import path
from .views import educationinfo_create,eudcationinfo_list,educationinfo_detail,educationinfo_update,educationinfo_delete

app_name = 'education'

urlpatterns = [
    
   # requires student id
    path('educationinfo_create/<str:id>',educationinfo_create.createEducationInfo,name = 'educationinfo_create'),
    path('educationinfo_list',eudcationinfo_list.listEducationInfo,name = 'educationinfo_list'),
    # requires educationinformation id
    path('educationinfo_detail/<str:id>',educationinfo_detail.educationinfoDetail,name = 'educationinfo_detail'),
    # requires educationinformation id
    path('educationinfo_update/<str:id>',educationinfo_update.updateEducationInfo,name = 'educationinfo_update'),
   # requires educationinformation id
    path('educationinfo_delete/<str:id>',educationinfo_delete.deleteEducationInfo,name = 'educationinfo_delete'),

]