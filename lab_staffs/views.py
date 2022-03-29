from django.http import HttpResponse
from users.models import User

import logging
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import lab_staff_required
from hospital.models import Diagnosis, LabTest
from patients.models import PatientProfile
from .forms import labTestForm, labTestUpdateForm

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

@login_required
@lab_staff_required
def viewDiagnosis(request):
    logger.info('lab staff viewing diagnosis')
    diagnosis = Diagnosis.objects.filter(lab_test_status=True)
    context = {'diagnosis': diagnosis}
    return render(request, "lab_staffs/viewDiagnosis.html", context)

@login_required
@lab_staff_required
def approve_or_deny(request):
    if request.POST:
        if 'Approve' in request.POST:
            logger.info('lab staff approve lab test')
            messages.success(request, 'Lab test report approve!')
            return redirect('lab_staffs:createReport')
        elif 'Deny' in request.POST:
            logger.info('lab staff deny labtest')
            appid = request.POST.get('app_id')
            username = request.POST.get('dia')
            user = User.objects.get(username=username)
            patientProfile = PatientProfile.objects.get(user=user)
            userDia = Diagnosis.objects.get(patient=patientProfile, appointment_id=appid)
            userDia.lab_test_status = False
            userDia.save()
            messages.success(request, 'Lab test report deny!')
    return redirect('lab_staffs:viewDiagnosis')

@login_required
@lab_staff_required
def viewReport(request):
    logger.info('lab staff viewing report')
    report = LabTest.objects.all()
    context = {'report': report}
    return render(request, "lab_staffs/viewReport.html", context)

@login_required
@lab_staff_required
def createReport(request):
    if request.POST:
        createReportForm = labTestForm(request.POST)
        if createReportForm.is_valid():
            createReportForm.save()
            logger.info('lab staff create report')
            return redirect('lab_staffs:labstaff-home')
    else:
        createReportForm = labTestForm()
    context = {'createReportForm': createReportForm}
    return render(request, "lab_staffs/createReport.html", context)

@login_required
@lab_staff_required
def deleteAndUpdateReport(request):
    if request.POST:
        if 'Delete' in request.POST:
            dia_id = request.POST.get('dia_id')
            lab_test_deleted = LabTest.objects.get(diagnosis_id = dia_id)
            lab_test_deleted.delete()
            logger.info('lab staff delete report')
            return redirect('lab_staffs:viewReport')
        elif 'Update' in request.POST:
            dia_id = request.POST.get('dia_id')
            lab_test_update = LabTest.objects.get(diagnosis_id= dia_id)
            lab_test_update_form = labTestUpdateForm(instance=lab_test_update)
            context = {'updateReportForm':lab_test_update_form,
                       'dia_id':dia_id}
            return render(request, 'lab_staffs/updateReport.html', context)
    return redirect('lab_staffs:viewReport')

@login_required
@lab_staff_required
def updateReport(request, id):
    lab_test_update = LabTest.objects.get(diagnosis_id=id)
    if request.POST:
        print(lab_test_update)
        update_form = labTestUpdateForm(request.POST, instance=lab_test_update)
        if update_form.is_valid():
            update_form.save()
            logger.info('lab staff update report')
            return redirect('lab_staffs:viewReport')
        return HttpResponse('form unvalid')
    return redirect('lab_staffs:viewReport')