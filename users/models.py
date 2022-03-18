from datetime import date

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
    date_of_birth = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.username}'
