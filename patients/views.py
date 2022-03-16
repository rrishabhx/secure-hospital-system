import logging

from django.contrib.auth.decorators import login_required

from hospital.forms import AppointmentCreationForm
from hospital.models import Appointment
from patients.models import PatientProfile
from users.decorators import patient_required
from django.shortcuts import render, get_object_or_404

from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)


@login_required
@patient_required
def home(request):
    user = get_object_or_404(PatientProfile, pk=request.user.pk)
    logger.info(f"Inside home of {user}")
    appointment_form = AppointmentCreationForm()

    context = {
        'appointments': Appointment.objects.filter(patient=user),
        'appointment_form': appointment_form
    }

    return render(request, 'patients/home.html', context)
