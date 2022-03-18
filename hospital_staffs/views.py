from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreatePatientForm,ViewPatientForm,ViewPatientRecords,ViewLabRecords,CreateTransaction
from django.apps import apps


# Create your views here.
def home(request):
    #return HttpResponse("<h1>Hospital staff's Home page</h1>")
    return render(request,'hospital_staffs/home.html')
    
def createPatient(request):
    #return HttpResponse("<h1>Hospital staff's Home page</h1>")
    form  = CreatePatientForm()
    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'hospital_staffs/createPatient.html',context)
    
def viewPatient(request):
    #return HttpResponse("<h1>Hospital staff's Home page</h1>")
    form  = ViewPatientForm()
    context = {'form':form, 'prescription' : ["Enter Patient and Doctor for prescription"], 'diagnosis': ["Enter Patient and Doctor for prescription"]}
    if request.method == 'GET' and 'patientID' in request.GET and 'doctorId' in request.GET:
        form = ViewPatientForm(request.GET)
        if form.is_valid():
            model = apps.get_model('patients', 'PatientRecords')

            try:
                x = model.objects.filter(patientID = request.GET['patientID'], doctorId = request.GET['doctorId'])
                context['prescription'] = []
                context['diagnosis'] = []
                print('hello')
                for i in x.iterator():
                    
                    context['prescription'].append(i.prescription)
                    context['diagnosis'].append(i.diagnosis)
            except Exception as e:
                context['prescription'] = ["No information available as of now"]
                context['diagnosis'] = ["No information available as of now"]
            finally:
                render(request,'hospital_staffs/viewPatient.html',context)
                
    return render(request,'hospital_staffs/viewPatient.html',context)
    
def viewRecords(request):
    form = ViewPatientRecords()
    defText = 'Enter Patient Details fo records'
    context = {'form':form, 'records' : [[defText]*4]}
    print(request.GET)
    if request.method == 'GET' and 'patientID' in request.GET:
        form = ViewPatientRecords(request.GET)
        if form.is_valid():
            model = apps.get_model('patients', 'PatientRecords')
            try:
                x = model.objects.filter(patientID = request.GET['patientID'])
                context['records'] = []
                for i in x.iterator():
                    l = ['','','','']
                    l[0],l[1],l[2],l[3] = i.prescription, i.diagnosis, i.doctorId, i.labTestId
                    context['records'].append(l)
            except Exception as e:
                context['records'] = ["No information available as of now"]*4
            finally:
                render(request,'hospital_staffs/viewPatientRecords.html',context)
    return render(request,'hospital_staffs/viewPatientRecords.html',context)
    
    
def viewLabTests(request):
    form = ViewLabRecords()
    context = {'form':form, 'records' : [['Enter Patient Details fo records']*3]}
    if request.method == 'GET' and 'patientId' in request.GET:
        form = ViewLabRecords(request.GET)
        if form.is_valid():
            model = apps.get_model('lab_staffs', 'LabStaffProfile')
            try:
                x = model.objects.filter(patientId = request.GET['patientId'])
                context['records'] = []
                for i in x.iterator():
                    l = ['','','']
                    l[0],l[1],l[2] = i.testType, i.testResult, i.staffId
                    context['records'].append(l)
            except Exception as e:
                context['records'] = ["No information available as of now"]*3
            finally:
                render(request,'hospital_staffs/viewLabRecords.html',context)
    return render(request,'hospital_staffs/viewLabRecords.html',context)


def createTransaction(request):
    #return HttpResponse("<h1>Hospital staff's Home page</h1>")
    form  = CreateTransaction()
    if request.method == 'POST':
        form = CreateTransaction(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'hospital_staffs/createTransaction.html',context)
    
def approveTransaction(request):
    model = apps.get_model('patients', 'Transactions')
    context = {'transactions': []}
    if request.method == 'POST':
        try:
            flag = request.POST['id']
            y = model.objects.get(id = flag)
            y.status = 'completed'
            y.save()
            print(flag)
        except KeyError:
            print('KeyError')
    try:
        x = model.objects.filter(status = 'approved')
        for i in x.iterator():
            context['transactions'].append(i)
    except:
        context['transactions'] = [['Record not found']*3]
    return render(request,'hospital_staffs/approveTransaction.html',context)