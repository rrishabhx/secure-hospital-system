from django.db import models
from django.conf import settings


class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'Profile: {self.user.username}({self.user.user_type})'
