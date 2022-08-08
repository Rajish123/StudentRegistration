from django.db import models
from student.models import Student
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404



# Create your models here.
class EducationInformation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    symbol_number = models.CharField(max_length=50)
    board = models.CharField(max_length=50)
    institution_name  = models.CharField(max_length=50)
    cgpa = models.CharField(max_length=50)
    passed_year = models.CharField(max_length=50)

    class Meta:
        ordering = ('symbol_number',)
        verbose_name = "EducationInformation"
        verbose_name_plural = "EducationInformations"

    @staticmethod
    def get_all_educationinfo():
        return EducationInformation.objects.all()

    @staticmethod
    def get_educationinfo_by_id(id):
        try:
            return EducationInformation.objects.get(id = id)
        except ObjectDoesNotExist:
            return None