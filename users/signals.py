from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from patients.models import PatientProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_patient_profile(sender, instance, created, **kwargs):
    if created:
        PatientProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_patient_profile(sender, instance, **kwargs):
    instance.patientprofile.save()
