# from pyexpat import model
from django.db import models
# from datetime import date
# from django.conf import settings
# from django.contrib.auth.models import AbstractUser
# from pandas import notnull

# class AdminProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.user_type + str() + self.user.username

class Employee(models.Model):
    EMPLOYEE_TYPE_CHOICES = (
        ('hospital_staff', 'Hospital Staff'),
        ('doctor', 'Doctor'),
        ('insurance_staff', 'Insurance Staff'),
        ('lab_staff', 'Lab Staff'),
        ('administrators', 'Administrators')
    )

    employee_type = models.CharField(max_length=20, default='hospital_staff', choices=EMPLOYEE_TYPE_CHOICES)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    # password = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.employee_type

class Deleted_Employees(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    employee_type = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.first_name
    