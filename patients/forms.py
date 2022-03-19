from django import forms
from datetime import datetime


class ProfileForm(forms.Form):
    username = forms.CharField(
        label='Username', max_length=100, required=False, disabled=True)
    email = forms.CharField(label='Email', max_length=100,
                            required=False, disabled=True)
    address = forms.CharField(label='Address', max_length=100, required=False)
    insurance = forms.CharField(
        label='Insurance', max_length=100, required=False)


class AppointmentForm(forms.Form):
    title = forms.CharField(label="Title", max_length=150)
    description = forms.CharField(label="Description", max_length=1000)
    doctor = forms.ChoiceField(label="Select Doctor", choices=[(
        '', "Choose an option"), ('No', "No Preference"), ('D1', "Doctor1"), ('D2', "Doctor2")])
    date_posted = datetime.now()


class InsuranceForm(forms.Form):
    claimAmount = forms.IntegerField(label='Claim Amount')
