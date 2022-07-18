from django.contrib import admin
from batch.models import Batch

# Register your models here.
@admin.register(Batch)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['batch_name',]
