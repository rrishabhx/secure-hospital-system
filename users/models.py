from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.conf import settings
from datetime import datetime
import random


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('hospital_staff', 'Hospital Staff'),
        ('doctor', 'Doctor'),
        ('insurance_staff', 'Insurance Staff'),
        ('lab_staff', 'Lab Staff'),
        ('administrator', 'Administrator'),
    )

    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, default='patient', choices=USER_TYPE_CHOICES)
    date_of_birth = models.DateField(default=date.today, validators=[MaxValueValidator(limit_value=date.today)])

    def __str__(self):
        return f'{self.username}'


class Code(models.Model):
    number = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        number_list = [i for i in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = ''.join(str(item) for item in code_items)

        self.number = code_string
        super().save(*args, **kwargs)


class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'logs'
