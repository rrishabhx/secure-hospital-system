from django import forms

from doctors.models import DoctorProfile
from hospital.models import Appointment, InsuredPatient, InsuranceClaim, Transaction, InsuranceRequest, Diagnosis


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

    def __init__(self, patient, *args, **kwargs):
        super(InsuranceClaimForm, self).__init__(*args, **kwargs)
        self.fields['diagnosis'].queryset = Diagnosis.objects.filter(patient=patient)


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('diagnosis', 'amount', 'approved', 'completed')


class InsuranceRequestForm(forms.ModelForm):
    class Meta:
        model = InsuranceRequest
        fields = ('insurance_policy',)
