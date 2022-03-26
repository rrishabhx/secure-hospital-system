from django.http import HttpResponse
from users.models import User

import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import lab_staff_required
from hospital.models import Diagnosis, LabTest
from .forms import labTestForm

logger = logging.getLogger(__name__)

@login_required
@lab_staff_required
# Create your views here.
def home(request):
    logger.info(f"Inside home of {request.user}")
    user = request.user.labstaffprofile
    logger.info(f"User object: {user}")

    diagnosis = Diagnosis.objects.all()

    context = {"diagnosis":diagnosis}

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
    context = {}
    return render(request, "lab_staffs/viewDiagnosis.html", context)

def createReport(request):
    if request.method == "POST":
        createReportForm = labTestForm(request.POST, instance=LabTest)
        if createReportForm.is_valid():
            report_data = createReportForm.cleaned_data
            report_obj = LabTest(**report_data)
            report_obj.save()
            return redirect('lab_staffs:labstaff-home')
    else:
        createReportForm = labTestForm()
    context = {'createReportForm': createReportForm}
    return render(request, "lab_staffs/createReport.html", context)

def deleteReport(request):
    test = request.POST.get('search')

def updateReport(request):
    list = [1, 2, 3, 4]
    context = {"list":list}
    return render(request, "lab_staffs/updateReport.html", context)

def approveTest(request):
    # if request.method == "POST":
    #     if 'username' in request.POST and request.POST['username']:
    #         username = request.POST['username']
    #         user = User.objects.get(username=username)
    #         patientProfile = PatientProfile.objects.get(user=user)
    #         patientDiagnosis_list = get_list_or_404(Diagnosis, patient=patientProfile)
    #         context = {"patientDiagnosis": patientDiagnosis_list}
    #     else:
    #         context = {'Error': 'Error, empty patient name'}
    context = {}

    return render(request, "lab_staffs/approveTest.html", context)