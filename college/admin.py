from django.contrib import admin
from college.models import CollegeInformation

# Register your models here.
@admin.register(CollegeInformation)
class CollegeInfoAdmin(admin.ModelAdmin):
    list_display = ['student','batch','semester','faculty','tu_registration_number','symbol_number']
