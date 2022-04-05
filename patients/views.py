import ast
import logging

import requests
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from hospital.models import Appointment, Diagnosis, LabTest, InsuranceClaim, Transaction, InsurancePolicy, \
    InsuranceRequest
from patients.forms import AppointmentForm, InsuranceClaimForm, TransactionForm, InsuredPatientForm, \
    InsuranceRequestForm
from secure_hospital_system import settings
from users.decorators import patient_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

from users.forms import UserUpdateForm, CodeForm

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
            messages.error(request, 'Error Processing Request. Please re-check your inputs')
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
    if request.session.get('code', '00000') != request.user.code.number:
        return redirect('patients:verify-patient', hfunc='insurance')

    patient_profile = request.user.patientprofile
    insured_patient = None
    if hasattr(patient_profile, 'insuredpatient'):
        insured_patient = request.user.patientprofile.insuredpatient

    if request.method == 'POST':
        form = InsuranceClaimForm(patient_profile, request.POST)
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
        form = InsuranceClaimForm(patient_profile)

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
    # if request.session.get('code', '00000') != request.user.code.number:
    #     return redirect('patients:verify-patient', hfunc='transactions')
    #
    # if request.method == 'POST':
    #     form = TransactionForm(request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         messages.success(request, 'Transaction complete')
    #         return redirect('patients:transactions')
    # else:
    #     form = TransactionForm()
    #
    # context = {
    #     'transactions': Transaction.objects.filter(patient=request.user.patientprofile),
    #     'form': form
    # }
    #
    # return render(request, 'patients/transactions.html', context=context)
    return redirect('patients:receipt')


def verify_patient(request, hfunc):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')

    if pk:
        user = User.objects.get(pk=pk)
        code = user.code
        code_user = f"{user.username}: {user.code}"

        if not request.POST:
            # send email
            send_otp_through_email(user, code)
            print(code_user)

        if form.is_valid():
            num = form.cleaned_data.get('number')

            if str(code) == num:
                code.save()
                request.session['code'] = str(code)
                messages.success(request, f'{user.username} Verification Successful!')
                return redirect(f'patients:{hfunc}')
            else:
                messages.error(request, f'Incorrect OTP!! Please try again.')
                return redirect(f'patients:{hfunc}')
    else:
        messages.warning(request, "Internal Server Error. Try logging-in Again...")
        return redirect('patients:home')

    messages.info(request, "If you don't receive OTP, please verify/update your Email in profile page")
    return render(request, 'users/verify.html', {'form': form})


def send_otp_through_email(user, otp):
    try:
        send_mail(subject="Dr. Yau's Clinic Email Verification Code", message=f"OTP: {otp}",
                  from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email])
    except:
        print(f"Unable to send OTP to {user.email}! Please update correct Email in Profile")


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


# @login_required
# @patient_required
# def requestPolicy(request):
#    form = InsuredPatientForm()
#    user = request.user.patientprofile
#    if request.method == 'POST':
#        try:
#            form = InsuredPatientForm(request.POST)
#            flag = request.POST['insurance_policy']
#            policy = InsurancePolicy.objects.get(id=flag)
#            amount = policy.max_amount
#            if form.is_valid():
#                if hasattr(user, 'insuredpatient'):
#                    insured_patient = request.user.patientprofile.insuredpatient
#                    insured_patient.insurance_policy = policy
#                    insured_patient.amount_available = amount
#                else:
#                    insured_patient = InsuredPatient(patient=user,
#                                             insurance_policy=policy, amount_available=amount)
#                insured_patient.save()
#                y = insured_patient
#                print(y.amount_available)
#                messages.success(request, 'Record Updated')
#        except Exception as e:
#            print(e)
#    context = {'form': form}
#    return render(request, 'patients/requestPolicy.html', context)

@login_required
@patient_required
def requestPolicy(request):
    form = InsuranceRequestForm()
    user = request.user.patientprofile
    if request.method == 'POST':
        try:
            form = InsuranceRequestForm(request.POST)
            if form.is_valid():
                policy = InsurancePolicy.objects.get(id=request.POST['insurance_policy'])
                req = InsuranceRequest(patient=user, insurance_policy=policy, approved=False)
                req.save()
                messages.success(request, 'Record Created')
        except Exception as e:
            print(e)
    context = {'form': form}
    return render(request, 'patients/requestPolicy.html', context)


@login_required
@patient_required
def receipt(request):
    model = Transaction
    context = {'transactions': []}
    try:
        x = model.objects.filter(approved='t', completed='t', patient=request.user.patientprofile)
        generateHreq(x, request)
        for i in x.iterator():
            context['transactions'].append(i)
    except:
        print('some issue')
    return render(request, 'patients/receipt.html', context)


def generateHreq(y, request):
    try:
        URL = 'http://ec2-54-176-204-18.us-west-1.compute.amazonaws.com:8080/api/queryallcars'
        r = requests.get(url=URL)
        js = r.json()
        l = []
        e = ast.literal_eval(js['response'])
        for i in e:
            d = {'patient': '', 'amount': '', 'staff': ''}
            check = i['Record']
            if check['owner'] == 'djangoapp':
                d['patient'] = check['make']
                d['amount'] = check['model']
                d['staff'] = check['colour']
                l.append(d)

        if len(y) != len(l):
            print("Transaction mismatch")

    except Exception as e:
        print(e)
