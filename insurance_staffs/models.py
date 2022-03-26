from django.conf import settings
from django.db import models


# Create your models here.
class InsuranceStaffProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.user_type}: {self.user.username}'
