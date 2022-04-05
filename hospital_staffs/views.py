from random import randint

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hospital.models import Diagnosis
from users.decorators import hospital_staff_required
from .forms import CreatePatientForm, ViewPatientForm, ViewPatientRecords, CreateTransaction, ViewLabRecords, \
    ViewAppointment
from django.contrib import messages
from django.apps import apps
from users.forms import UserUpdateForm


@login_required
@hospital_staff_required
def home(request):
    return render(request, 'hospital_staffs/home.html')


@login_required
@hospital_staff_required
def createPatient(request):
    all_diagnosis = Diagnosis.objects.all()
    ids = [d.appointment.id for d in all_diagnosis]
    form = CreatePatientForm(ids)
    model1 = apps.get_model('hospital', 'Appointment')
    model2 = apps.get_model('hospital', 'Diagnosis')
    print(form.fields)
    if request.method == 'POST':
        try:
            flag = request.POST['appointment']
            y = model1.objects.get(id=flag)
            x = model2.objects.create(appointment=y, doctor=y.doctor, patient=y.patient)
            x.save()
            messages.success(request, 'New Record Created')
        except KeyError:
            print('KeyError')
        except Exception as e:
            print('some issue')
    context = {'form': form}
    return render(request, 'hospital_staffs/createPatient.html', context)


@login_required
@hospital_staff_required
def viewPatient(request):
    form = ViewPatientForm()
    context = {'form': form, 'prescription': [],
               'diagnosis': [], 'checklistP': False, 'checklistD': False}
    if request.method == 'GET' and 'patient' in request.GET:
        form = ViewPatientForm(request.GET)
        if form.is_valid():
            model = apps.get_model('hospital', 'Diagnosis')
            try:
                x = model.objects.filter(patient=request.GET['patient'])
                context['prescription'] = []
                context['diagnosis'] = []
                for i in x.iterator():
                    if (i.prescription):
                        context['prescription'].append(i.prescription)
                    if (i.details):
                        context['diagnosis'].append(i.details)
                if (context['prescription']):
                    context['checklistP'] = True
                if (context['diagnosis']):
                    context['checklistD'] = True


            except Exception as e:
                context['prescription'] = ["No information available as of now"]
                context['diagnosis'] = ["No information available as of now"]
            finally:
                render(request, 'hospital_staffs/viewPatient.html', context)

    return render(request, 'hospital_staffs/viewPatient.html', context)


@login_required
@hospital_staff_required
def viewRecords(request):
    form = ViewPatientRecords()
    defText = 'Enter Patient Details fo records'
    context = {'form': form, 'records': [], 'checklist': False}
    if request.method == 'GET' and 'patient' in request.GET:
        form = ViewPatientRecords(request.GET)
        if form.is_valid():
            model = apps.get_model('hospital', 'Diagnosis')
            try:
                x = model.objects.filter(patient=request.GET['patient'])
                context['records'] = []
                for i in x.iterator():
                    l = ['', '', '', '']
                    l[0], l[1], l[2], l[3] = i.prescription, i.details, i.doctor, i.lab_tests_recommended
                    context['records'].append(l)
                    context['checklist'] = True
            except Exception as e:
                context['records'] = ["No information available as of now"]
            finally:
                render(request, 'hospital_staffs/viewPatientRecords.html', context)
    return render(request, 'hospital_staffs/viewPatientRecords.html', context)


@login_required
@hospital_staff_required
def viewLabTests(request):
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
                render(request, 'hospital_staffs/viewLabRecords.html', context)
    return render(request, 'hospital_staffs/viewLabRecords.html', context)


@login_required
@hospital_staff_required
def createTransaction(request):
    model = apps.get_model('hospital_staffs', 'HospitalStaffProfile')
    x = model.objects.filter(user=request.user.id)
    val = 0
    for i in x.iterator():
        val = i.id
        break
    form = CreateTransaction()
    if request.method == 'POST':
        form = CreateTransaction(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Record Created')
    context = {'form': form}
    return render(request, 'hospital_staffs/createTransaction.html', context)


@login_required
@hospital_staff_required
def approveTransaction(request):
    model = apps.get_model('hospital', 'Transaction')
    context = {'transactions': []}
    if request.method == 'POST':
        try:
            flag = request.POST['id']
            y = model.objects.get(id=flag)
            y.completed = True
            y.save()
            generateHreq(y, request)
            messages.success(request, 'Transaction completed!')
            print(flag)
        except KeyError:
            print('KeyError')
    try:
        x = model.objects.filter(approved='t', completed=None)
        for i in x.iterator():
            context['transactions'].append(i)
    except:
        context['transactions'] = [['Record not found'] * 3]
    return render(request, 'hospital_staffs/approveTransaction.html', context)


@login_required
@hospital_staff_required
def approveAppointment(request):
    model = apps.get_model('hospital', 'Appointment')
    context = {'transactions': []}
    if request.method == 'POST':
        try:
            flag = request.POST['id']
            y = model.objects.get(id=flag)
            y.status = True
            y.save()
            messages.success(request, 'Appointment Approved!')
            print(flag)
        except KeyError:
            print('KeyError')
    try:
        x = model.objects.filter(status=None)
        for i in x.iterator():
            context['transactions'].append(i)
    except:
        context['transactions'] = []
    return render(request, 'hospital_staffs/approveAppointment.html', context)


@login_required
@hospital_staff_required
def appointment(request):
    form = ViewAppointment()
    context = {
        'appointments': [],
        'form': form
    }
    if request.method == 'GET' and 'doctor' in request.GET:
        form = ViewAppointment(request.GET)
        if form.is_valid():
            model = apps.get_model('hospital', 'Appointment')
            try:
                x = model.objects.filter(doctor=request.GET['doctor'], status='t')
                context['appointments'] = x
            except Exception as e:
                print(e)
            finally:
                render(request, 'hospital_staffs/appointments.html', context)
    return render(request, 'hospital_staffs/appointments.html', context=context)


@login_required
@hospital_staff_required
def profile(request):
    print("Inside hospitalstaff profile")
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

    return render(request, 'hospital_staffs/profile.html', context)


def generateHreq(y, request):
    try:
        URL = 'http://ec2-54-176-204-18.us-west-1.compute.amazonaws.com:8080/api/addcar'
        value = randint(0, 100000)
        inval = 'CAR' + str(value)
        r = requests.post(url=URL, json={'carid': inval, 'make': str(y.patient), 'model': str(y.amount),
                                         'colour': str(request.user), 'owner': 'djangoapp'})
        print(inval)
    except Exception as e:
        print(e)
