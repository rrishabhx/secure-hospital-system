# from django.contrib.auth.forms import UserCreationForm
# from datetime import datetime
from django import forms
from .models import Employee


# from administrators.models import AdminProfile

class CreateEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(label="Email Address", max_length=40, required=True)
    # dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(max_length=10, label="Phone Number")

    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'employee_type', 'dob', 'email', 'phone_number']
