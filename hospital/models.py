from django.db import models

from patients.models import PatientProfile


class Appointment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, primary_key=True)
    scheduled_date = models.DateTimeField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-scheduled_date', '-created']

    def __str__(self):
        return self.title
