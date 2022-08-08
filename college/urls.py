from django.urls import path
from .views import collegeinfo_create,collegeinfo_list,collegeinfo_update,collegeinfo_detail, collegeinfo_delete

app_name = 'college_info'

urlpatterns = [
    # requires student id
    path('collegeinfo_create/<str:id>',collegeinfo_create.createCollegeInfo,name = 'collegeinfo_create'),
    # requires collegeinfo id
    path('collegeinfo_list',collegeinfo_list.listCollegeInfo, name = 'collegeinfo_list'),
    path('collegeinfo_update/<str:id>',collegeinfo_update.updateCollegeInfo, name = 'collegeinfo_update'),
    path('collegeinfo_detail/<str:id>',collegeinfo_detail.collegeInfoDetail,name = 'collegeinfo_detail'),
    path('collegeinfo_delete/<str:id>',collegeinfo_delete.deleteCollegeInfo,name = 'collegeinfo_delete')

]
