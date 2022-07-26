from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile','citizenship','gender','blood_group','temp_address','perm_address','dob','is_active','is_alumi','picture']




