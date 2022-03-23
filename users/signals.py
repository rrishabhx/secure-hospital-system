import logging

from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from patients.models import PatientProfile
from hospital_staffs.models import HospitalStaffProfile
from doctors.models import DoctorProfile
from insurance_staffs.models import InsuranceStaffProfile
from lab_staffs.models import LabStaffProfile

User = get_user_model()
logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_usertype_profile(sender, instance, created, **kwargs):
    logger.info("Inside user-profile creation signal")
    if created:
        if instance.user_type == 'patient':
            PatientProfile.objects.create(user=instance)
        elif instance.user_type == 'hospital_staff':
            HospitalStaffProfile.objects.create(user=instance)
        elif instance.user_type == 'doctor':
            DoctorProfile.objects.create(user=instance)
        elif instance.user_type == 'insurance_staff':
            InsuranceStaffProfile.objects.create(user=instance)
        elif instance.user_type == 'lab_staff':
            LabStaffProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_usertype_profile(sender, instance, **kwargs):
    logger.info("Inside user-profile save signal")
    if instance.user_type == 'patient':
        instance.patientprofile.save()
    elif instance.user_type == 'hospital_staff':
        instance.hospitalstaffprofile.save()
    elif instance.user_type == 'doctor':
        instance.doctorprofile.save()
    elif instance.user_type == 'insurance_staff':
        instance.insurancestaffprofile.save()
    elif instance.user_type == 'lab_staff':
        instance.labstaffprofile.save()
