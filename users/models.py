from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_hospital_staff = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_lab_staff = models.BooleanField(default=False)
    is_insurance_staff = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
