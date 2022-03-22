from django.utils import timezone

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from patients.models import PatientProfile
from doctors.models import DoctorProfile

'''
Many-to-one relationship example:
if a Car model has a Manufacturer – that is, a Manufacturer makes multiple cars but each Car only has one Manufacturer

from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # ...

'''


# TODO: Review doctor availability, Transactions, Insurance functionality
class Appointment(models.Model):
    """
    Appointment requested: status=False
    Appointment approved: status=True
    """
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
    scheduled_date = models.DateTimeField(validators=[MinValueValidator(limit_value=timezone.now)])
    appointment_details = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-scheduled_date', '-created']

    def __str__(self):
        return f"{self.patient},{self.doctor},{self.appointment_details}"


class Diagnosis(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    prescription = models.TextField(null=True, blank=True)
    lab_tests_recommended = models.TextField(null=True, blank=True)
    lab_test_status = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)


class LabTest(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    lab_tests_recommended = models.OneToOneField(Diagnosis, on_delete=models.CASCADE)
    lab_test_report = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)


class InsurancePolicy(models.Model):
    name = models.CharField(max_length=100)
    max_amount = models.PositiveSmallIntegerField(default=100,
                                                  validators=[MinValueValidator(1), MaxValueValidator(1000)])


class InsuranceClaim(models.Model):
    patient = models.OneToOneField(PatientProfile, on_delete=models.CASCADE)
    insurance_policy = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
