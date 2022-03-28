import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hospital.forms import AppointmentCreationForm, LabTestRecommendationForm
from hospital.models import Appointment, Diagnosis, LabTest
from patients.models import PatientProfile
from doctors.models import DoctorProfile
from users.decorators import patient_required, doctor_required

logger = logging.getLogger(__name__)


# @login_required
# @patient_required
# def request_appointment(request):
#     appointment_form = AppointmentCreationForm()
#
#     if request.method == 'POST':
#         print("Patient requesting appointment")
#
#         appointment_form = AppointmentCreationForm(request.POST)
#         if appointment_form.is_valid():
#             print("Valid Patient:Appointment form")
#
#             appointment_data = appointment_form.cleaned_data
#             appointment_data['patient'] = PatientProfile.objects.get(user=request.user)
#
#             print(f"Appointment form data: {appointment_data}")
#
#             appointment_obj = Appointment(**appointment_data)
#             appointment_obj.save()
#         else:
#             print("Patient: Appointment form INVALID")
#
#     return redirect('patient-home')
#
#
# @login_required
# @doctor_required
# def request_diagnosis(request):
#
#     if request.method == 'POST':
#         print("Doctor creating diagnosis")
#
#         recommendation_form = LabTestRecommendationForm(request.POST)
#         if recommendation_form.is_valid():
#             print("Valid Doctor:Diagnosis form")
#
#             data = recommendation_form.cleaned_data
#             data['doctor'] = DoctorProfile.objects.get(user=request.user)
#
#             print(f"Diagnosis form data: {data}")
#
#             diagnosis_obj = Diagnosis(**data)
#             diagnosis_obj.save()
#         else:
#             print("Doctor: Diagnosis form INVALID")
#
#     return redirect('doctor-home')
