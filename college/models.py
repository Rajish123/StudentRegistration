from django.db import models
from student.models import Student
from batch.models import Batch, Semester, Faculty
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.

class CollegeInformation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)
    faculty= models.ForeignKey(Faculty, on_delete = models.DO_NOTHING)
    tu_registration_number = models.CharField(max_length=100)
    symbol_number = models.CharField(max_length=50)

    class Meta:
        ordering = ('symbol_number',)
        verbose_name = "CollegeInformation"
        verbose_name_plural = "CollegeInformations"

    @staticmethod
    def get_all_collegeinfo():
        return CollegeInformation.objects.all()

    @staticmethod
    def get_collegeinfo_by_id(id):
        try:
            return CollegeInformation.objects.get(id = id)
        except ObjectDoesNotExist:
            return None