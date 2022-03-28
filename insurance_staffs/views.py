from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from hospital.models import InsuranceClaim, InsurancePolicy
from insurance_staffs.forms import InsurancePolicyForm
from users.decorators import insurance_staff_required
from users.forms import UserUpdateForm


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


@login_required
@insurance_staff_required
def policies(request):
    print(f"{request.user}: Insurance policies page")
    if request.method == 'POST':
        print(request.POST)
        form = InsurancePolicyForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'New Insurance Policy Created')
            return redirect('insurance_staffs:policies')
        else:
            print(f"{request.user}: Invalid insurance policy form data- {form.cleaned_data}")
    else:
        form = InsurancePolicyForm()

    context = {
        'form': form,
        'policies': InsurancePolicy.objects.all()
    }
    return render(request, 'insurance_staffs/policies.html', context=context)


@login_required
@insurance_staff_required
def profile(request):
    print("Inside insurance-staff profile")
    user = request.user
    insurance_staff_profile = request.user.insurancestaffprofile

    if request.method == 'POST':
        print("Request type: POST")
        u_form = UserUpdateForm(request.POST, instance=user)

        if u_form.is_valid():
            u_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('insurance_staffs:profile')
    else:
        print(f"Request type: GET")
        u_form = UserUpdateForm(instance=user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'insurance_staffs/profile.html', context)
