

from django.http import HttpResponse
from django.shortcuts import render
import logging
from django.apps import apps

from django.contrib.auth.decorators import login_required

from hospital.forms import LabTestRecommendationForm
from hospital.models import Appointment, Diagnosis, LabTest
from doctors.models import DoctorProfile
from users.decorators import doctor_required
from django.shortcuts import render, get_object_or_404
from .forms import ProfileForm, UpdatePatientForm,ViewLabRecords
from django.contrib import messages

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
#     print(f"Inside home of {request.user}")
#     user = get_object_or_404(DoctorProfile, user=request.user)
#     print(f"User object: {user}")
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
    print(f"Inside home of {request.user}")
    user = request.user.doctorprofile
    print(f"User object: {user}")

    recommendation_form = LabTestRecommendationForm()

    context = {
        'appointments': Appointment.objects.filter(doctor=user),
        'diagnosis': Diagnosis.objects.filter(doctor=user),
        'lab_tests': LabTest.objects.filter(doctor=user),
        'recommendation_form': recommendation_form
    }
    return render(request, 'doctors/home.html', context)


def prescriptions(request):
    form = UpdatePatientForm()
    context = {'form': form, 'records': [], 'checklist':False}
    if request.method == 'POST' and 'patient' not in request.POST:
        model = apps.get_model('hospital', 'Diagnosis')
        try:
            flag = request.POST['id']
            y = model.objects.get(id=flag)
            if('prescription'in request.POST):
                if not request.POST['prescription']:
                    y.prescription = None
                    print(y.prescription)
                    print('a')
                y.prescription = request.POST['prescription']
                print(request.POST['prescription'])
            if('details' in request.POST):
                if not request.POST['details']:
                    y.details = None
                y.details = request.POST['details']  
            if('lab' in request.POST):
                if not request.POST['lab']:
                    y.lab_tests_recommended = None
                y.lab_tests_recommended = request.POST['lab']               
            y.save()
        except KeyError:
            print('KeyError')
        finally:
                render(request, 'doctors/prescriptions.html', context)
    if request.method == 'POST' and 'patient' in request.POST:
        user = request.user.doctorprofile
        form = UpdatePatientForm(request.POST)
        if form.is_valid():
            model = apps.get_model('hospital', 'Diagnosis')
            try:
                x = model.objects.filter(patient=request.POST['patient'], doctor = user)
                context['records'] = []
                for i in x.iterator():
                    context['records'].append(i)
                    context['checklist'] = True
            except Exception as e:
                print('Some issue')
            finally:
                render(request, 'doctors/prescriptions.html', context)
    return render(request, 'doctors/prescriptions.html', context)


def diagnosis(request):
    print(f"{request.user}: Diagnosis page")

    diagnosis_list = Diagnosis.objects.filter(doctor=request.user.doctorprofile)
    print(f"{request.user}: Previous diagnosis: {diagnosis_list}")

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
    form = ViewLabRecords()
    context = {'form': form, 'records': [],'checklist': False}
    if request.method == 'GET' and 'patient' in request.GET:
        form = ViewLabRecords(request.GET)
        if form.is_valid():
            model = apps.get_model('hospital', 'LabTest')
            try:
                x = model.objects.filter(patient=request.GET['patient'])
                context['records'] = []
                for i in x.iterator():
                    l = ['', '', '']
                    l[0], l[1], l[2] = i.doctor, i.lab_test_report, i.created
                    context['records'].append(l)
                    context['checklist'] = True
            except Exception as e:
                context['records'] = ["No information available as of now"]
            finally:
                render(request, 'doctors/reports.html', context)
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
    


