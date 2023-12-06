from django.db import models
from author.models import Author

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    # bio = models.TextField()
    # phone_no = models.CharField(max_length=15)
    # email = models.EmailField()
    # image = models.ImageField(upload_to='profile_pics')
    author = models.OneToOneField(Author, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.name