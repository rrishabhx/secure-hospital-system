from django import forms

from doctors.models import DoctorProfile
from hospital.models import Appointment, InsuredPatient, InsuranceClaim, Transaction


class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(label="Select Doctor (Optional)",
                                    required=False, queryset=DoctorProfile.objects.all())
    scheduled_date = forms.DateTimeField(label='Please choose a date',
                                         widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Appointment

        fields = ('doctor', 'scheduled_date', 'appointment_details')


class InsuredPatientForm(forms.ModelForm):
    class Meta:
        model = InsuredPatient
        fields = ['insurance_policy']


class InsuranceClaimForm(forms.ModelForm):
    class Meta:
        model = InsuranceClaim
        fields = ('claim_amount', 'diagnosis')


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('diagnosis', 'amount', 'approved', 'completed')
