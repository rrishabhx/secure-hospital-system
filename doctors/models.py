from django.conf import settings
from django.db import models


# Create your models here.
class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    staffId = models.ForeignKey('hospital_staffs.HospitalStaffProfile',on_delete=models.CASCADE,null=True)
    timeSlot = models.DateTimeField(auto_now_add=True,null=True)
    patientId = models.ForeignKey('patients.PatientProfile',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.user.user_type}: {self.user.username}'

