from django import forms
from datetime import datetime

from doctors.models import DoctorProfile
from hospital.models import Appointment


class ProfileForm(forms.Form):
    username = forms.CharField(
        label='Username', max_length=100, required=False, disabled=True)
    email = forms.CharField(label='Email', max_length=100,
                            required=False, disabled=True)
    address = forms.CharField(label='Address', max_length=100, required=False)
    insurance = forms.CharField(
        label='Insurance', max_length=100, required=False)


class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(label="Select Doctor", required=False, queryset=DoctorProfile.objects.all())
    scheduled_date = forms.DateTimeField(label='Please choose a date',
                                         widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Appointment

        fields = ('doctor', 'scheduled_date', 'appointment_details')


class InsuranceForm(forms.Form):
    claimAmount = forms.IntegerField(label='Claim Amount')
