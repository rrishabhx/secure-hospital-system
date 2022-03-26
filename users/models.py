from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.conf import settings
from datetime import datetime


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
    date_of_birth = models.DateField(default=date.today, validators=[MaxValueValidator(limit_value=date.today)])

    def __str__(self):
        return f'{self.username}'
        
        
        
class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(default = datetime.now, blank = True)
    class Meta:
        db_table = 'logs'
