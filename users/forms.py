from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from patients.models import PatientProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    dob = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)

    class Meta:
        model = User
        fields = ['user_type', 'username', 'first_name', 'last_name', 'email', 'dob', 'password1',
                  'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    dob = forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)

    class Meta:
        model = User
        fields = ['username', 'email']


class PatientProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['image']
