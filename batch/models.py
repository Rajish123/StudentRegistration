from django.db import models

# Create your models here.
class Batch(models.Model):
    batch_name = models.CharField(max_length=50)


    @staticmethod
    def get_batch_by_id(id):
        return Batch.objects.get(id = id)

    @staticmethod
    def get_all_batch():
        return Batch.objects.all()

    def __str__(self):
        return self.batch_name