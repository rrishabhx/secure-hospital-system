from django.conf import settings
from django.db import models


# Create your models here.
class LabStaffProfile(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    testType = models.CharField(max_length=30,null=True,blank = True)
    testResult = models.TextField(null=True,blank = True)
    staffId = models.ForeignKey('hospital_staffs.HospitalStaffProfile',on_delete=models.CASCADE,null=True,blank = True)
    patientId = models.ForeignKey('patients.PatientProfile',on_delete=models.CASCADE,null=True,blank = True)
    class Meta:
        db_table = 'labtest'
