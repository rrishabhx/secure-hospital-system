from django import forms
from .models import Appointment


class AppointmentCreationForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ('status', 'created', )
