import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hospital.forms import AppointmentCreationForm
from hospital.models import Appointment
from patients.models import PatientProfile
from users.decorators import patient_required

logger = logging.getLogger(__name__)


@login_required
@patient_required
def request_appointment(request):
    appointment_form = AppointmentCreationForm()

    if request.method == 'POST':
        logger.info("Patient requesting appointment")

        appointment_form = AppointmentCreationForm(request.POST)
        if appointment_form.is_valid():
            logger.info("Valid Patient:Appointment form")

            appointment_data = appointment_form.cleaned_data
            appointment_data['patient'] = PatientProfile.objects.get(user=request.user)

            logger.info(f"Appointment form data: {appointment_data}")

            appointment_obj = Appointment(**appointment_data)
            appointment_obj.save()
        else:
            logger.error("Patient: Appointment form INVALID")

    return redirect('patient-home')
