from django.db import models

from patients.models import PatientProfile


class Appointment(models.Model):
    scheduled_date = models.DateTimeField(null=True)
    status = models.BooleanField(default=False,null=True)
    staffId = models.ForeignKey('hospital_staffs.HospitalStaffProfile',on_delete=models.CASCADE,null=True)
    patientId = models.ForeignKey('patients.PatientProfile',on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    appointmentType = models.CharField(max_length=100,null=True)

    class Meta:
        ordering = ['-scheduled_date', '-created']
        db_table = 'appointments'

    def __str__(self):
        return self.title
