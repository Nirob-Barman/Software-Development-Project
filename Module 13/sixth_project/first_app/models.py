from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField(max_length=50)
    marks = models.IntegerField()
    father_name = models.CharField(max_length=20, default="Nirob Barman")

    # def __str__(self):
    #     return self.name
    def __str__(self):
        return f'Roll: {self.roll} - {self.name}'
