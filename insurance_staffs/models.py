from django.conf import settings
from django.db import models


# Create your models here.
class InsuranceStaffProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employeeId = models.ForeignKey('hospital_staffs.HospitalStaffProfile',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.user.user_type}: {self.user.username}'
    class Meta:
        db_table = 'insuranceStaff'

class insuranceClaim(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    claimAmount = models.DecimalField(max_digits=6, decimal_places=4,null=True)
    status = models.CharField(max_length=30,null=True)
    staffId = models.ForeignKey('insurance_staffs.InsuranceStaffProfile',on_delete=models.CASCADE,null=True)
    patientId = models.ForeignKey('patients.PatientProfile',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'{self.user.user_type}: {self.user.username}'
    class Meta:
        db_table = 'insuranceClaims'


class InsurancePolicies(models.Model):
    companyName = models.CharField(max_length=30, null=True) 
    policyName = models.CharField(max_length=50, null=True)
    benefitsAvailable = models.TextField(null=True)

    def __str__(self):
        return self.policyName
    class Meta:
        db_table = 'insurancePolicies'

