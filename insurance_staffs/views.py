from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from hospital.models import InsuranceClaim
from users.decorators import insurance_staff_required


@login_required
@insurance_staff_required
def home(request):
    print(f"Inside home of {request.user}")
    return redirect('insurance_staffs:claims')


@login_required
@insurance_staff_required
def claims(request):
    print(f"{request.user}: Claims page")
    if request.method == 'POST':
        print(request.POST)
        try:
            if 'approve_claim' in request.POST:
                obj = InsuranceClaim.objects.get(id=int(request.POST.get('approve_claim')))
                obj.status = True
                obj.insured_patient.amount_available -= obj.claim_amount
            elif 'deny_claim' in request.POST:
                obj = InsuranceClaim.objects.get(id=int(request.POST.get('deny_claim')))
                obj.status = False

            obj.insured_patient.save()
            obj.save()
        except Exception as e:
            print(f"An error occurred while trying to update insurance claim status: {e}")
            return redirect('insurance_staffs:claims')

        messages.success(request, 'Insurance claims status have been updated')
        return redirect('insurance_staffs:claims')

    context = {
        'claims': InsuranceClaim.objects.filter(status__isnull=True).order_by('-created'),
        'old_claims': InsuranceClaim.objects.filter(status__isnull=False).order_by('-created')
    }
    return render(request, 'insurance_staffs/claims.html', context=context)


def policies(request):
    return None
