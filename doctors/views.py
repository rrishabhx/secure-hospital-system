

from django.http import HttpResponse
from django.shortcuts import render
import logging

from django.contrib.auth.decorators import login_required

from hospital.forms import AppointmentCreationForm
from hospital.models import Appointment, Diagnosis, LabTest
from doctors.models import DoctorProfile
from users.decorators import doctor_required
from django.shortcuts import render, get_object_or_404

from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)


@login_required
@doctor_required
# Create your views here.
def home(request):
    logger.info(f"Inside home of {request.user}")
    user = get_object_or_404(DoctorProfile, user=request.user)
    logger.info(f"User object: {user}")
    context = {
        'appointments': Appointment.objects.filter(doctor=user),
        'diagnosis': Diagnosis.objects.filter(doctor=user),
        'lab_tests': LabTest.objects.filter(doctor=user),
    }
    return render(request, 'doctors/home.html', context)
