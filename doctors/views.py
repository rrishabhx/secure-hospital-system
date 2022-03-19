

from django.http import HttpResponse
from django.shortcuts import render
import logging

from django.contrib.auth.decorators import login_required

from hospital.forms import LabTestRecommendationForm
from hospital.models import Appointment, Diagnosis, LabTest
from doctors.models import DoctorProfile
from users.decorators import doctor_required
from django.shortcuts import render, get_object_or_404
from .forms import ProfileForm

from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)

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

@login_required
@doctor_required
# Create your views here.
# def home(request):
#     logger.info(f"Inside home of {request.user}")
#     user = get_object_or_404(DoctorProfile, user=request.user)
#     logger.info(f"User object: {user}")
#
#     recommendation_form = LabTestRecommendationForm()
#
#     context = {
#         'appointments': Appointment.objects.filter(doctor=user),
#         'diagnosis': Diagnosis.objects.filter(doctor=user),
#         'lab_tests': LabTest.objects.filter(doctor=user),
#         'recommendation_form': recommendation_form
#     }
#     return render(request, 'doctors/home.html', context)
def home(request):
    logger.info(f"Inside home of {request.user}")
    user = request.user.doctorprofile
    logger.info(f"User object: {user}")

    recommendation_form = LabTestRecommendationForm()

    context = {
        'appointments': Appointment.objects.filter(doctor=user),
        'diagnosis': Diagnosis.objects.filter(doctor=user),
        'lab_tests': LabTest.objects.filter(doctor=user),
        'recommendation_form': recommendation_form
    }
    return render(request, 'doctors/home.html', context)


def prescriptions(request):
    logger.info(f"{request.user}: Prescriptions page")
    if request.method == 'POST':
        form = LabTestRecommendationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            data['doctor'] = request.user.doctorprofile

            logger.info(f"{request.user}: New prescription details- {data}")
            obj = Diagnosis(**data)
            obj.save()

            messages.success(request, 'New Prescripotion Created')
            return redirect('doctors:prescriptions')
        else:
            logger.error(f"{request.user}: Invalid form data- {form.data}")
    else:
        form = LabTestRecommendationForm()

    context = {
        'prescriptions': Diagnosis.objects.filter(doctor=request.user.doctorprofile),
        'form': form
    }
    return render(request, 'doctors/prescriptions.html', context=context)


def diagnosis(request):
    logger.info(f"{request.user}: Diagnosis page")

    diagnosis_list = Diagnosis.objects.filter(doctor=request.user.doctorprofile)
    logger.info(f"{request.user}: Previous diagnosis: {diagnosis_list}")

    context = {
        'diagnosis_list': diagnosis_list,
    }
    return render(request, 'doctors/diagnosis.html', context=context)


def appointments(request):
    user = request.user.doctorprofile
    context = {
        'appointments': Appointment.objects.filter(doctor=user),
    }

    return render(request, 'doctors/appointments.html', context=context)


def reports(request):
    context = {
        'reports': reports_list
    }
    return render(request, 'doctors/reports.html', context=context)

def profile(request):
    form = ProfileForm()
    # profile = PatientProfile.objects.all()[0]
    #form = ProfileForm(initial={'username': profile.user.username, 'email': profile.user.email,
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
    return render(request, 'doctors/profile.html', context=context)
