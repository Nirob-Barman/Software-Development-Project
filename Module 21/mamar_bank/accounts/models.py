from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE, GENDER_TYPE
# Create your models here.

# ACCOUNT_TYPE = (
#     ('Savings', 'Savings'),
#     ('Current', 'Current'),
# )

# GENDER_TYPE = (
#     ('Male', 'Male'),
#     ('Female', 'Female'),
#     ('Other', 'Other'),
#     ('Prefer not to say', 'Prefer not to say'),
#     ('Prefer to self-describe', 'Prefer to self-describe'),
#     ('Prefer not to answer', 'Prefer not to answer'),
#     ('Prefer to not say', 'Prefer to not say'),
#     ('Prefer to not disclose', 'Prefer to not disclose'),
#     ('Prefer not to disclose', 'Prefer not to disclose'),
#     ('Prefer to disclose', 'Prefer to disclose'),
# )


class UserBankAccount(models.Model):
    user = models.OneToOneField(
        User, related_name='account', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    # In Django models, when you set null=True for a field, it means that the corresponding database column can have empty (NULL) values.
    # blank=True: This parameter is used for form validation in Django, indicating that a form can be submitted with this field left blank.
    birth_date = models.DateField(null=True, blank=True)
    # gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    gender = models.CharField(max_length=50, choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    # balance for monetary values with a default of 0, max 12 digits, and 2 decimal places.
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.account_no)


class UserAddress(models.Model):
    user = models.OneToOneField(
        User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user.email)
