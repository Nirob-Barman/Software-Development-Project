from django.db import models

# Create your models here.
class BankSettings(models.Model):
    is_bankrupt = models.BooleanField(default=False)

    def __str__(self):
        return f"Bank Settings - Bankrupt: {self.is_bankrupt}"