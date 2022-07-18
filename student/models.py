from tabnanny import verbose
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    mobile = models.CharField(max_length = 10, unique=True, db_index=True)
    citizenship = models.CharField(max_length=20, unique=True, db_index=True)
    gender = models.CharField(max_length = 10)
    blood_group = models.CharField(max_length=5)
    temp_address = models.CharField(max_length=150, null= True, blank = True)
    perm_address = models.CharField(max_length=150)
    dob = models.CharField(max_length=150)
    is_active = models.BooleanField(default = True)
    is_alumi = models.BooleanField(default=False)
    picture = models.ImageField(upload_to = 'student_picture', default = 'scooter.png', null = True, blank = True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'student'
        verbose_name_plural = "students"

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_student():
        return Student.objects.all()

    @staticmethod
    def get_student_by_id(id):
        return Student.objects.get(id = id)