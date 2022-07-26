from django.db import models
from student.models import Student
from batch.models import Batch, Semester, Faculty

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