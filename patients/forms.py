from django import forms

from doctors.models import DoctorProfile
from hospital.models import Appointment, InsuredPatient
from patients.models import PatientProfile


class PatientProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['image', 'address']


class InsurancePolicyUpdateForm(forms.ModelForm):
    class Meta:
        model = InsuredPatient
        fields = ['insurance_policy']


class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(label="Select Doctor", required=False, queryset=DoctorProfile.objects.all())
    scheduled_date = forms.DateTimeField(label='Please choose a date',
                                         widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Appointment

        fields = ('doctor', 'scheduled_date', 'appointment_details')


class InsuranceForm(forms.Form):
    claimAmount = forms.IntegerField(label='Claim Amount')
