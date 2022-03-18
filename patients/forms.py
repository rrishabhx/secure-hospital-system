from cProfile import label
from ctypes import addressof
from multiprocessing import Value
from django import forms


class ProfileForm(forms.Form):
    username = forms.CharField(
        label='Username', max_length=100, required=False, disabled=True)
    email = forms.CharField(label='Email', max_length=100,
                            required=False, disabled=True)
    address = forms.CharField(label='Address', max_length=100, required=False)
    insurance = forms.CharField(
        label='Insurance', max_length=100, required=False)


class InsuranceForm(forms.Form):
    claimAmount = forms.IntegerField(label='Claim Amount')
