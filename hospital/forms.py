from django import forms
from .models import Appointment


class AppointmentCreationForm(forms.ModelForm):
    scheduled_date = forms.DateField(label='What is your birth date?',
                                     widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Appointment

        fields = ('doctor', 'scheduled_date', 'appointment_details')
