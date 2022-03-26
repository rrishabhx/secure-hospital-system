from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreatePatientForm, ViewPatientForm, ViewPatientRecords, CreateTransaction, ViewLabRecords
from django.contrib import messages
from django.apps import apps


# Create your views here.
def home(request):
    return render(request, 'hospital_staffs/home.html')


def createPatient(request):
    form = CreatePatientForm()
    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Record Created')
    context = {'form': form}
    return render(request, 'hospital_staffs/createPatient.html', context)


def viewPatient(request):
    form = ViewPatientForm()
    context = {'form': form, 'prescription': ["Enter Patient and Doctor for prescription"],
               'diagnosis': ["Enter Patient and Doctor for prescription"]}
    if request.method == 'GET' and 'patient' in request.GET and 'doctor' in request.GET:
        form = ViewPatientForm(request.GET)
        if form.is_valid():
            model = apps.get_model('hospital', 'Diagnosis')
            print(request.GET)
            try:
                x = model.objects.filter(patient=request.GET['patient'], doctor=request.GET['doctor'])
                print(x)
                print('hel')
                context['prescription'] = []
                context['diagnosis'] = []
                print('hello')
                for i in x.iterator():
                    context['prescription'].append(i.prescription)
                    context['diagnosis'].append(i.details)
            except Exception as e:
                context['prescription'] = ["No information available as of now"]
                context['diagnosis'] = ["No information available as of now"]
            finally:
                render(request, 'hospital_staffs/viewPatient.html', context)

    return render(request, 'hospital_staffs/viewPatient.html', context)


def viewRecords(request):
    form = ViewPatientRecords()
    defText = 'Enter Patient Details fo records'
    context = {'form': form, 'records': [[defText] * 4]}
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
            except Exception as e:
                context['records'] = ["No information available as of now"]
            finally:
                render(request, 'hospital_staffs/viewPatientRecords.html', context)
    return render(request, 'hospital_staffs/viewPatientRecords.html', context)


def viewLabTests(request):
    form = ViewLabRecords()
    context = {'form': form, 'records': [['Enter Patient Details fo records'] * 3]}
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
            except Exception as e:
                context['records'] = ["No information available as of now"]
            finally:
                render(request, 'hospital_staffs/viewLabRecords.html', context)
    return render(request, 'hospital_staffs/viewLabRecords.html', context)


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


def approveTransaction(request):
    model = apps.get_model('hospital', 'Transaction')
    context = {'transactions': []}
    if request.method == 'POST':
        try:
            flag = request.POST['id']
            y = model.objects.get(id=flag)
            y.completed = True
            y.save()
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


def approveAppointment(request):
    model = apps.get_model('hospital', 'Appointment')
    context = {'transactions': []}
    if request.method == 'POST':
        try:
            flag = request.POST['id']
            y = model.objects.get(id=flag)
            y.status = True
            y.save()
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
