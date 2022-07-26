from django.contrib import admin
from batch.models import Batch,Semester,Faculty

# Register your models here.
@admin.register(Batch)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['batch_name',]

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['semester_name',]

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['faculty_name',]

