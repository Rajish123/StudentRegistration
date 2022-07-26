from django.contrib import admin
from education.models import EducationInformation

# Register your models here.
@admin.register(EducationInformation)
class EducationInfoAdmin(admin.ModelAdmin):
    list_display = ['student','symbol_number','board','institution_name','cgpa','passed_year']