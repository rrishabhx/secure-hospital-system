from django.conf import settings
from django.db import models

# Create your models here.
# class LabStaffProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     testType = models.CharField(max_length=30,null=True)
#     testResult = models.TextField(null=True)
#     staffId = models.ForeignKey('hospital_staffs.HospitalStaffProfile',on_delete=models.CASCADE,null=True)
#     patientId = models.ForeignKey('patients.PatientProfile',on_delete=models.CASCADE,null=True)
#     def __str__(self):
#         return f'{self.user.user_type}: {self.user.username}'
#     class Meta:
#         db_table = 'labtest'

class LabStaffProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    staffId = models.ForeignKey('hospital_staffs.HospitalStaffProfile',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.user.user_type}: {self.user.username}'

class LabTestReport(models.Model):
    testType = models.CharField(max_length=30, null=True)
    testResult = models.TextField(null=True)
    staffId = models.ForeignKey('hospital_staffs.HospitalStaffProfile', on_delete=models.CASCADE, null=True)
    patientId = models.ForeignKey('patients.PatientProfile', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'labtest'


