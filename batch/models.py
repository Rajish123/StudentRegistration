from django.db import models
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.
class Batch(models.Model):
    batch_name = models.CharField(max_length=50)


    class Meta:
        verbose_name = 'Batch_name'
        verbose_name_plural = "Batch_names"


    @staticmethod
    def get_batch_by_id(id):
        try:
            return Batch.objects.get(id = id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_all_batch():
        return Batch.objects.all()

    def __str__(self):
        return self.batch_name

class Semester(models.Model):
    semester_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'Semester_name'
        verbose_name_plural = "Semester_names"

    
    @staticmethod
    def get_all_semester():
        return Semester.objects.all()

    @staticmethod
    def get_semester_by_id(id):
        try:
            return Semester.objects.get(id = id)
        except ObjectDoesNotExist:
            return None

    def __str__(self):
        return self.semester_name

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Faculty_name'
        verbose_name_plural = "Faculty_names"

    @staticmethod
    def get_all_fauclty():
        return Faculty.objects.all()

    @staticmethod
    def get_faculty_by_id(id):
        try:
            return Faculty.objects.get(id = id)
        except ObjectDoesNotExist:
            return None

    def __str__(self):
        return self.faculty_name   
