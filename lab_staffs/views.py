from django.http import HttpResponse
from users.models import User
import logging
from django.shortcuts import render
from users.decorators import lab_staff_required
from hospital.models import Diagnosis, LabTest

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    logger.info(f"Inside home of {request.user}")
    user = request.user.labstaffprofile
    logger.info(f"User object: {user}")

    context = {'staffFile':user}
    return render(request, "lab_staffs/labstaff-home.html", context)

def viewDiagnosis(request):
    if request.method == "POST":
        # if 'username' in request.POST and request.POST['username']:
        #     username = request.POST['username']
        #     user = User.objects.get(username=username)
        #     patientProfile = Diagnosis.objects.get(user=user)
        #     patientDiagnosis_list = get_list_or_404(Diagnosis, patient=patientProfile)
        #     context = {"patientDiagnosis": patientDiagnosis_list}
        # else:
        #     context = {'Error': 'Error, empty patient name'}
        diagnosis = Diagnosis.objects.all()

    return render(request, "lab_staffs/viewDiagnosis.html", context)

def createReport(request, patientID, authorization):
    if request.method == "POST":
        if 'patient_name' in request.POST and request.POST['patient_name']:
            username = request.POST['patient_name']
            user = User.objects.get(username=username)
            patientProfile = PatientProfile.objects.get(user=user)
            patientDiagnosis_list = get_list_or_404(Diagnosis, patient=patientProfile)
            context = {"patientDiagnosis": patientDiagnosis_list}
        else:
            context = {'Error': 'Error, empty patient name'}
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

def approveTest(request):
    if request.method == "POST":
        if 'username' in request.POST and request.POST['username']:
            username = request.POST['username']
            user = User.objects.get(username=username)
            patientProfile = PatientProfile.objects.get(user=user)
            patientDiagnosis_list = get_list_or_404(Diagnosis, patient=patientProfile)
            context = {"patientDiagnosis": patientDiagnosis_list}
        else:
            context = {'Error': 'Error, empty patient name'}

    return render(request, "lab_staffs/approveTest.html", context)