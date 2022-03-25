from django.db import models
from django.conf import settings
from PIL import Image


# TODO: Add models for Payments and Transactions

class PatientProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    # insurance = models.OneToOneField(InsurancePolicy, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.user_type}: {self.user.username}'

    # Overriding save() method with image resizing
    def save(self, *args, **kwargs):
        super(PatientProfile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Transactions(models.Model):
    patientID = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, null=True)
    staffId = models.ForeignKey('hospital_staffs.HospitalStaffProfile', on_delete=models.CASCADE, null=True)
    status = models.BooleanField(null=True, blank=True)
    transactionAmount = models.DecimalField(max_digits=12, decimal_places=4, null=True)
