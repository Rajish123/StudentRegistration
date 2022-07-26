from django.contrib import admin
from family.models import FamilyInformation

# Register your models here.
@admin.register(FamilyInformation)
class FamilyInfoAdmin(admin.ModelAdmin):
    list_display = ['student','fathers_name','mothers_name','fathers_number','mothers_number','guardian_name','guardian_relation']
