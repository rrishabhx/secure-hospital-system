from django import forms
from .models import Appointment
from .models import Diagnosis


class AppointmentCreationForm(forms.ModelForm):
    scheduled_date = forms.DateField(label='Please choose a date',
                                     widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Appointment

        fields = ('doctor', 'scheduled_date', 'appointment_details')


class LabTestRecommendationForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ('patient', 'appointment', 'details', 'prescription', 'lab_tests_recommended')
