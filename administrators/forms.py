# from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Employee
# from administrators.models import AdminProfile

class CreateEmployeeForm(forms.ModelForm):
    email = forms.EmailField(label="Email Address")
    dob = forms.DateField(label='Employee Birth Date', widget=forms.SelectDateWidget)
    phone_number = forms.IntegerField(label="Phone Number")
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'employee_type', 'email', 'dob', 'phone_number']