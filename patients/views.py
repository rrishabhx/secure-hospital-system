import logging

from django.contrib.auth.decorators import login_required

from hospital.models import Appointment, Diagnosis, LabTest, InsuredPatient, Transaction, InsuranceClaim
from users.decorators import patient_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model

from users.forms import UserUpdateForm
from .forms import InsuredPatientForm, AppointmentForm, InsuranceClaimForm, TransactionForm

User = get_user_model()

logger = logging.getLogger(__name__)


@login_required
@patient_required
def home(request):
    print(f"Inside home of {request.user}")
    return redirect('patients:appointments')


@login_required
@patient_required
def appointments(request):
    print(f"{request.user}: Appointments page")
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment_data = form.cleaned_data
            appointment_data['patient'] = request.user.patientprofile

            print(f"{request.user}: New appointment details- {appointment_data}")
            appointment_obj = Appointment(**appointment_data)
            appointment_obj.save()

            messages.success(request, 'New Appointment Requested')
            return redirect('patients:appointments')
        else:
            print(f"{request.user}: Invalid form data- {form.data}")
    else:
        form = AppointmentForm()

    context = {
        'appointments': Appointment.objects.filter(patient=request.user.patientprofile),
        'form': form
    }
    return render(request, 'patients/appointments.html', context=context)


@login_required
@patient_required
def diagnosis(request):
    print(f"{request.user}: Diagnosis page")

    diagnosis_list = Diagnosis.objects.filter(patient=request.user.patientprofile)
    print(f"{request.user}: Previous diagnosis: {diagnosis_list}")

    context = {
        'diagnosis_list': diagnosis_list,
    }
    return render(request, 'patients/diagnosis.html', context=context)


@login_required
@patient_required
def prescriptions(request):
    print(f"{request.user}: Prescriptions page")

    diagnosis_list = Diagnosis.objects.filter(patient=request.user.patientprofile)
    print(f"{request.user}: Previous diagnosis: {diagnosis_list}")

    context = {
        'diagnosis_list': diagnosis_list,
    }
    return render(request, 'patients/prescriptions.html', context=context)


@login_required
@patient_required
def lab_test_reports(request):
    print(f"{request.user}: Lab Test Reports page")

    lab_tests = LabTest.objects.filter(patient=request.user.patientprofile)
    print(f"{request.user}: Previous Lab Reports: {lab_tests}")

    context = {
        'lab_tests': lab_tests,
    }
    return render(request, 'patients/lab_test_reports.html', context=context)


@login_required
@patient_required
def insurance(request):
    print(f"{request.user}: Insurance page")

    patient_profile = request.user.patientprofile
    insured_patient = None
    if hasattr(patient_profile, 'insuredpatient'):
        insured_patient = request.user.patientprofile.insuredpatient

    if request.method == 'POST':
        form = InsuranceClaimForm(request.POST)
        if form.is_valid():
            insurance_claim_data = form.cleaned_data
            if insured_patient:
                insurance_claim_data['insured_patient'] = insured_patient

                insurance_claim_obj = InsuranceClaim(**insurance_claim_data)
                insurance_claim_obj.save()

                messages.success(request, 'New Insurance Claim Filed')
            else:
                print(f"{request.user}: Patient not insured. Only God can save you!!")
                messages.error(request, 'Patient not insured. Only God can save you!!')

            return redirect('patients:insurance')
        else:
            print(f"{request.user}: Invalid insurance form data- {form.data}")
    else:
        form = InsuranceClaimForm()

    context = {
        'form': form
    }

    if insured_patient:
        context['insurance_claims'] = InsuranceClaim.objects.filter(insured_patient=insured_patient)

    return render(request, 'patients/insurance.html', context=context)


@login_required
@patient_required
def transactions(request):
    print(f"{request.user}: Transactions page")

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            messages.success(request, 'Transaction complete')
            return redirect('patients:transactions')
    else:
        form = TransactionForm()

    context = {
        'transactions': Transaction.objects.filter(patient=request.user.patientprofile),
        'form': form
    }

    return render(request, 'patients/transactions.html', context=context)


@login_required
@patient_required
def profile(request):
    print("Inside patient profile")
    user = request.user
    patient_profile = request.user.patientprofile

    if request.method == 'POST':
        print("Request type: POST")
        u_form = UserUpdateForm(request.POST, instance=user)
        i_form = InsuredPatientForm(request.POST, instance=patient_profile.insuredpatient)

        if u_form.is_valid() and i_form.is_valid():
            u_form.save()
            i_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        print(f"Request type: GET")
        u_form = UserUpdateForm(instance=user)
        i_form = InsuredPatientForm()

        if hasattr(patient_profile, 'insuredpatient'):
            print(f"{patient_profile} has the 'insuredpatient' attribute")
            i_form = InsuredPatientForm(instance=patient_profile.insuredpatient)

    context = {
        'u_form': u_form,
        'i_form': i_form,
    }

    return render(request, 'patients/profile.html', context)
