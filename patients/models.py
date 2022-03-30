from django.db import models
from django.conf import settings
from PIL import Image


class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.user_type}: {self.user.username}'
