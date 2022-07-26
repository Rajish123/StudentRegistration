from django.db import models
from student.models import Student
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.

class FamilyInformation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=50)
    mothers_name = models.CharField(max_length=50)
    fathers_number = models.CharField(max_length=50)
    mothers_number = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length=50)
    guardian_relation = models.CharField(max_length=50)

    class Meta:
        verbose_name = "FamilyInformation"
        verbose_name_plural = "FamilyInformations"

    @staticmethod
    def get_all_familyinfo():
        return FamilyInformation.objects.all()

    @staticmethod
    def get_familyinfo_by_id(id):
        try:
            return FamilyInformation.objects.get(id = id)
        except ObjectDoesNotExist:
            return None                                                