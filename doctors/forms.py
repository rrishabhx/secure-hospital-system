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

