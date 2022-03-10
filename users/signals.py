from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from doctors.models import DoctorProfile
from patients.models import PatientProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_patient_profile(sender, instance, created, **kwargs):
    print("Inside patient creation signal")
    if created:
        if instance.user_type == 'patient':
            PatientProfile.objects.create(user=instance)
        elif instance.user_type == 'doctor':
            DoctorProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_patient_profile(sender, instance, **kwargs):
    print("Inside patient save signal")
    if instance.user_type == 'patient':
        instance.patientprofile.save()
    elif instance.user_type == 'doctor':
        instance.doctorprofile.save()
