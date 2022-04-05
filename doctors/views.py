import logging
from django.apps import apps

from django.contrib.auth.decorators import login_required

from hospital.forms import LabTestRecommendationForm
from hospital.models import Appointment, Diagnosis, LabTest
from users.decorators import doctor_required
from django.shortcuts import render, redirect
from .forms import ProfileForm, UpdatePatientForm, ViewLabRecords
from django.contrib import messages
from users.forms import UserUpdateForm

from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)


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
@login_required
@doctor_required
def home(request):
    print(f"Inside home of {request.user}")
    return redirect('doctors:appointments')


@login_required
@doctor_required
def prescriptions(request):
    diag = apps.get_model('hospital', 'Diagnosis')
    user = request.user.doctorprofile
    plist = []
    for i in diag.objects.all():
        if i.doctor == user:
            plist.append(i.patient.pk)
    print(plist, 'hello')
    form = UpdatePatientForm(plist)
    context = {'form': form, 'records': [], 'checklist': False}
    if request.method == 'POST' and 'patient' not in request.POST:
        model = apps.get_model('hospital', 'Diagnosis')
        try:
            flag = request.POST['id']
            y = model.objects.get(id=flag)
            if 'prescription' in request.POST:
                if not request.POST['prescription']:
                    y.prescription = None
                    print(y.prescription)
                    print('a')
                y.prescription = request.POST['prescription']
                print(request.POST['prescription'])
            if 'details' in request.POST:
                if not request.POST['details']:
                    y.details = None
                y.details = request.POST['details']
            if 'lab' in request.POST:
                if not request.POST['lab']:
                    y.lab_tests_recommended = None
                else:
                    if not request.POST['lab'] == 'None':
                        y.lab_tests_recommended = request.POST['lab']

            y.save()
        except KeyError:
            print('KeyError')
        finally:
            render(request, 'doctors/prescriptions.html', context)
    if request.method == 'POST' and 'patient' in request.POST:
        user = request.user.doctorprofile
        # form = UpdatePatientForm(request.POST)
        # if form.is_valid():
        model = apps.get_model('hospital', 'Diagnosis')
        try:
            x = model.objects.filter(patient=request.POST['patient'], doctor=user)
            context['records'] = []
            for i in x.iterator():
                context['records'].append(i)
                context['checklist'] = True
        except Exception as e:
            print('Some issue')
        finally:
            render(request, 'doctors/prescriptions.html', context)
    return render(request, 'doctors/prescriptions.html', context)


@login_required
@doctor_required
def diagnosis(request):
    print(f"{request.user}: Diagnosis page")

    diagnosis_list = Diagnosis.objects.filter(doctor=request.user.doctorprofile)
    print(f"{request.user}: Previous diagnosis: {diagnosis_list}")

    context = {
        'diagnosis_list': diagnosis_list,
    }
    return render(request, 'doctors/diagnosis.html', context=context)


@login_required
@doctor_required
def appointments(request):
    user = request.user.doctorprofile
    context = {
        'appointments': Appointment.objects.filter(doctor=user),
    }

    return render(request, 'doctors/appointments.html', context=context)


@login_required
@doctor_required
def reports(request):
    form = ViewLabRecords()
    context = {'form': form, 'records': [], 'checklist': False}
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


@login_required
@doctor_required
def profile(request):
    print("Inside doctor profile")
    user = request.user

    if request.method == 'POST':
        print("Request type: POST")
        u_form = UserUpdateForm(request.POST, instance=user)

        if u_form.is_valid():
            u_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('doctors:profile')
    else:
        print(f"Request type: GET")
        u_form = UserUpdateForm(instance=user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'doctors/profile.html', context)
