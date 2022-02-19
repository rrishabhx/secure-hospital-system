from django.db import models
from django.conf import settings
from PIL import Image


class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'Profile: {self.user.username}({self.user.user_type})'

    # Overriding save() method with image resizing
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
