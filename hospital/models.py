from django.db import models

from patients.models import PatientProfile
from doctors.models import DoctorProfile


class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    scheduled_date = models.DateTimeField()
    appointment_details = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-scheduled_date', '-created']

    def __str__(self):
        return f"P:{self.patient},D:{self.doctor},Apt:{self.appointment_details}"
