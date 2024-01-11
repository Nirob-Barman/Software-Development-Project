from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images')
    # specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    specialization = models.ManyToManyField(Specialization)
    # designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    designation = models.ManyToManyField(Designation)
    # available_time = models.ManyToManyField(AvailableTime)
    # available_time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE, null=True, blank=True)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    # meet_link = models.URLField(null=True, blank=True)
    meet_link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"


STAR_CHOICES = [
    ('⭐️', '⭐'),
    ('⭐️⭐', '⭐⭐'),
    ('⭐️⭐️⭐', '⭐⭐⭐'),
    ('⭐️⭐️⭐️⭐', '⭐⭐⭐⭐'),
    ('⭐️⭐️⭐️⭐️⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    # rating = models.IntegerField()
    # comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)
    def __str__(self):
        return f"{self.reviewer} - {self.doctor} - {self.rating}"
        # return f"{self.reviewer.user.first_name} - {self.doctor.user.first_name}"