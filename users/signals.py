import logging

from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from administrators.models import AdministratorProfile
from hospital.models import InsurancePolicy, InsuredPatient
from patients.models import PatientProfile
from hospital_staffs.models import HospitalStaffProfile
from doctors.models import DoctorProfile
from insurance_staffs.models import InsuranceStaffProfile
from lab_staffs.models import LabStaffProfile
from users.models import Log
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from datetime import datetime
from django.utils import timezone

User = get_user_model()
logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_usertype_profile(sender, instance, created, **kwargs):
    print("Inside user-profile creation signal")
    if created:
        if instance.user_type == 'patient':
            PatientProfile.objects.create(user=instance)

            if not InsurancePolicy.objects.exists():
                base_insurance_policy = InsurancePolicy(name='Free Government Insurance', max_amount=100)
                base_insurance_policy.save()
            else:
                base_insurance_policy = InsurancePolicy.objects.get(name='Free Government Insurance')

            insured_patient = InsuredPatient(patient=instance.patientprofile,
                                             insurance_policy=base_insurance_policy, amount_available=100)
            insured_patient.save()

        elif instance.user_type == 'hospital_staff':
            HospitalStaffProfile.objects.create(user=instance)
        elif instance.user_type == 'doctor':
            DoctorProfile.objects.create(user=instance)
        elif instance.user_type == 'insurance_staff':
            InsuranceStaffProfile.objects.create(user=instance)
        elif instance.user_type == 'lab_staff':
            LabStaffProfile.objects.create(user=instance)
        elif instance.user_type == 'administrator':
            AdministratorProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_usertype_profile(sender, instance, **kwargs):
    print("Inside user-profile save signal")
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
    # elif instance.user_type == 'administrator':
    #     instance.administratorprofile.save()


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    try:
        print('user {} logged in through page {}'.format(user.username, request.META.get('HTTP_REFERER')))
        # if user.user_type == 'patient':
        log = Log(user = user, date = datetime.now(tz=timezone.utc))
        log.save()
    except:
        print('something went wrong')


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    try:
        print('user {} logged in failed through page {}'.format(credentials.get('username'),
                                                                request.META.get('HTTP_REFERER')))
    except:
        print('something went wrong')

    # al = Log.objects.all()
    # for i in al:
    #    print(i.user, i.date)


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    try:
        print('user {} logged out through page {}'.format(user.username, request.META.get('HTTP_REFERER')))
    except:
        print('something went wrong')
