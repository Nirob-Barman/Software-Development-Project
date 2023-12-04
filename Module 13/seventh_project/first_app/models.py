from django.db import models

# Create your models here.


class StudentModel(models.Model):
    roll = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self):
        return f'{self.roll} - {self.name}'
