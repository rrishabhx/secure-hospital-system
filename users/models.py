from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('hospital_staff', 'Hospital Staff'),
        ('doctor', 'Doctor'),
        ('insurance_staff', 'Insurance Staff'),
        ('lab_staff', 'Lab Staff'),
        ('administrator', 'Administrator'),
    )

    user_type = models.CharField(max_length=20, default='patient', choices=USER_TYPE_CHOICES)
