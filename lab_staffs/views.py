from django.http import HttpResponse

from users.forms import UserUpdateForm
from users.models import User

import logging
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import lab_staff_required
from hospital.models import Diagnosis, LabTest
from patients.models import PatientProfile
from .forms import LabTestCreateForm, LabTestUpdateForm

logger = logging.getLogger(__name__)


@login_required
@lab_staff_required
# Create your views here.
def home(request):
    logger.info(f"Inside home of {request.user}")
    return redirect('lab_staffs:viewDiagnosis')


@login_required
@lab_staff_required
def viewDiagnosis(request):
    logger.info('lab staff viewing diagnosis')
    diagnosis = Diagnosis.objects.filter(lab_test_status__isnull=True, lab_tests_recommended__isnull=False)
    context = {'diagnosis': diagnosis}
    return render(request, "lab_staffs/viewDiagnosis.html", context)


@login_required
@lab_staff_required
def approve_or_deny(request):
    if request.POST:
        if 'Approve' in request.POST:
            logger.info('lab staff approve lab test')
            messages.success(request, 'Lab test report approved!')
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
            messages.info(request, 'Lab test report denied!')
    return redirect('lab_staffs:viewDiagnosis')


@login_required
@lab_staff_required
def viewReport(request):
    logger.info('lab staff viewing report')
    reports = LabTest.objects.all()
    context = {'reports': reports}
    return render(request, "lab_staffs/viewReport.html", context)


@login_required
@lab_staff_required
def createReport(request):
    if request.POST:
        createReportForm = LabTestCreateForm(request.POST)
        if createReportForm.is_valid():
            lab_test_data = createReportForm.cleaned_data
            lab_test_data['patient'] = lab_test_data.get('diagnosis').patient
            lab_test_data['doctor'] = lab_test_data.get('diagnosis').doctor

            lab_tes_obj = LabTest(**lab_test_data)
            lab_tes_obj.save()
            lab_tes_obj.diagnosis.lab_test_status = True
            lab_tes_obj.diagnosis.save()

            messages.success(request, f"Lab Test created for {lab_test_data['patient']}")
            return redirect('lab_staffs:home')
        else:
            messages.error(request, f"Please check the input data")
            return redirect('lab_staffs:createReport')
    else:
        createReportForm = LabTestCreateForm()
    context = {'createReportForm': createReportForm}
    return render(request, "lab_staffs/createReport.html", context)


@login_required
@lab_staff_required
def deleteAndUpdateReport(request):
    if request.POST:
        if 'Delete' in request.POST:
            dia_id = request.POST.get('dia_id')
            lab_test_deleted = LabTest.objects.get(diagnosis_id=dia_id)
            lab_test_deleted.delete()
            logger.info('lab staff delete report')
            return redirect('lab_staffs:viewReport')
        elif 'Update' in request.POST:
            dia_id = request.POST.get('dia_id')
            lab_test_update = LabTest.objects.get(diagnosis_id=dia_id)
            lab_test_update_form = LabTestUpdateForm(instance=lab_test_update)
            context = {'updateReportForm': lab_test_update_form,
                       'dia_id': dia_id}
            return render(request, 'lab_staffs/updateReport.html', context)
    return redirect('lab_staffs:viewReport')


@login_required
@lab_staff_required
def updateReport(request, id):
    lab_test_update = LabTest.objects.get(diagnosis_id=id)
    if request.POST:
        print(lab_test_update)
        update_form = LabTestUpdateForm(request.POST, instance=lab_test_update)
        if update_form.is_valid():
            update_form.save()
            logger.info('lab staff update report')
            return redirect('lab_staffs:viewReport')
        return HttpResponse('form unvalid')
    return redirect('lab_staffs:viewReport')


@login_required
@lab_staff_required
def profile(request):
    print("Inside lab_staff profile")
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

    return render(request, 'lab_staffs/profile.html', context)
