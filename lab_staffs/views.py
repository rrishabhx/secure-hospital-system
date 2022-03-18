from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from patients.models import PatientRecords


# Create your views here.
def home(request):
    patientRecord = PatientRecords.objects.all()
    context = {'patientRecords':patientRecord}
    return render(request, "lab_staffs/labstaff-home.html", context)

def viewDiagnosis(request):
    if 'patientID' in request.GET and request.GET['patientID']:
        patientID = request.GET['patientID']
        patientRecord = get_list_or_404(PatientRecords, id = patientID)
        context = {"patientRecord":patientRecord}
    else:
        context= {'Error':'Error, empty patient ID'}
    return render(request, "lab_staffs/viewDiagnosis.html", context)

def createReport(request, patientID, authorization):
    context = {}
    return render(request, "lab_staffs/createReport.html", context)

def deleteReport(request, patientID):
    if ():
        return HttpResponse("deleted")
    else:
        return HttpResponse("deleted failed")

def updateReport(request, patientID):
    context = {}
    return render(request, "lab_staffs/updateReport.html", context)

def approveTest(request, patientID, authorization, testType):
    if ():
        return HttpResponse("approve")
    else:
        return HttpResponse("approve failed")