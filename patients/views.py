import logging

from django.contrib.auth.decorators import login_required

from hospital.forms import AppointmentCreationForm
from hospital.models import Appointment, Diagnosis, LabTest
from patients.models import PatientProfile
from users.decorators import patient_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import PatientProfile
from.forms import ProfileForm, InsuranceForm, AppointmentForm


User = get_user_model()

logger = logging.getLogger(__name__)

appointments_list = [
    {
        'doctor': 'Dr. Mantis Tobbagan',
        'title': 'Covid-19',
        'description': 'No taste in food',
        'date_posted': 'Feb 27, 2022'
    },
    {
        'doctor': 'Dr. Jane Doe',
        'title': 'Cancer',
        'description': 'Too much blood loss',
        'date_posted': 'Feb 18, 2022'
    }
]

patients = [
    {
        'address': '1090440',
        'insurance': '1021039123',
        'user_id': '1',
        'id': 1,
        'image': '111'
    },
    {
        'address': '1090440',
        'insurance': '1021039123',
        'user_id': '1',
        'id': 1,
        'image': '111'
    }
]

insurance_claims = [
    {
        'id': 1,
        'claimAmount': 1999,
        'status': 'Rejected',
        'testResult': 'Pass',
        'PatientId_Id': 1,
        'staffId_Id': 2,
        'user_Id': 1
    },
    {
        'id': 2,
        'claimAmount': 2012,
        'status': 'Accepted',
        'testResult': 'Pass',
        'PatientId_Id': 1,
        'staffId_Id': 2,
        'user_Id': 1
    },
    {
        'id': 3,
        'claimAmount': 5455,
        'status': 'Pending',
        'testResult': 'Pass',
        'PatientId_Id': 1,
        'staffId_Id': 2,
        'user_Id': 1
    }
]

transactions_list = [
    {
        'Id': 1,
        'status': 'Rejected',
        'transactionAmount': 1525.55,
        'patientID_Id': 1,
        'stafID_Id': 3
    },
    {
        'Id': 2,
        'status': 'Accepted',
        'transactionAmount': 454.55,
        'patientID_Id': 1,
        'stafID_Id': 3
    },
    {
        'Id': 3,
        'status': 'Accepted',
        'transactionAmount': 564.55,
        'patientID_Id': 1,
        'stafID_Id': 3
    },
    {
        'Id': 4,
        'status': 'Pending',
        'transactionAmount': 454564.55,
        'patientID_Id': 1,
        'stafID_Id': 3
    },
    {
        'Id': 5,
        'status': 'Accepted',
        'transactionAmount': 456465444.55,
        'patientID_Id': 1,
        'stafID_Id': 3
    }
]

diagnosis_list = []
prescriptions_list = []
reports_list = [
    {
        'Id': 1,
        'testType': 'Type1',
        'testResult': 'All Ok',
        'patientID_Id': 1,
        'staffID_Id': 3,
        'userID_Id': 1
    },
    {
        'Id': 2,
        'testType': 'Type1',
        'testResult': 'All Ok',
        'patientID_Id': 1,
        'staffID_Id': 3,
        'userID_Id': 1
    },
    {
        'Id': 3,
        'testType': 'Type1',
        'testResult': 'All Ok',
        'patientID_Id': 1,
        'staffID_Id': 3,
        'userID_Id': 1
    },
    {
        'Id': 4,
        'testType': 'Type1',
        'testResult': 'All Ok',
        'patientID_Id': 1,
        'staffID_Id': 3,
        'userID_Id': 1
    },
]


# @login_required
# @patient_required
def home(request):

    logger.info(f"Inside home of {request.user}")
    user = get_object_or_404(PatientProfile, user=request.user)
    logger.info(f"User object: {user}")

    appointment_form = AppointmentCreationForm()
    context = {
        'appointments': appointments_list,
        'profile': profile,
        'appointment_form': appointment_form,
        'uform': ''
    }
    return render(request, 'patients/home.html', context=context)


def appointments(request):
    if(request.method == 'POST'):
        form = AppointmentForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            print(data)
            messages.success(request, 'New Appointment Requested')
            return redirect(reverse('patients:patient-home'))
    else:
        form = AppointmentForm()

    context = {
        'appointments': appointments_list,
        'form': form
    }
    return render(request, 'patients/appointments.html', context=context)


def diagnosis(request):
    context = {
        'diagnosis': diagnosis_list
    }

    return render(request, 'patients/diagnosis.html', context=context)


def prescriptions(request):
    context = {
        'prescriptions': prescriptions_list
    }

    return render(request, 'patients/prescriptions.html', context=context)


def reports(request):
    context = {
        'reports': reports_list
    }

    return render(request, 'patients/reports.html', context=context)


def insurance(request):
    if(request.method == 'POST'):
        form = InsuranceForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            print(data)
            messages.success(request, 'New Insurance Claim Filed')
            return redirect(reverse('patients:patient-home'))
    else:
        form = InsuranceForm()

    context = {
        'insurance_claims': insurance_claims,
        'form': form
    }

    return render(request, 'patients/insurance.html', context=context)


def transactions(request):
    context = {
        'transactions': transactions_list
    }

    return render(request, 'patients/transactions.html', context=context)


def profile(request):
    form = ProfileForm()
    # profile = PatientProfile.objects.all()[0]
    # form = ProfileForm(initial={'username': profile.user.username, 'email': profile.user.email,
    #                             'address': profile.address, 'insurance': profile.insurance})

    # if(request.method == 'POST'):
    #     form = ProfileForm(request.POST)
    #     if(form.is_valid()):
    #         data = form.cleaned_data
    #         profile.address = data['address']
    #         profile.insurance = data['insurance']
    #         profile.save()
    #         messages.success(request, 'Profile Updated')
    #         return redirect(reverse('patients:patient-home'))
    #     else:
    #         form = ProfileForm(initial={'username': profile.user.username, 'email': profile.user.email,
    #                                     'address': profile.address, 'insurance': profile.insurance})

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'patients/profile.html', context=context)
