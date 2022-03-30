from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from patients.models import PatientProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth = forms.DateField(label='What is your birth date?', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['user_type', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1',
                  'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    user_type = forms.CharField(disabled=True)
    date_of_birth = forms.DateField(label='What is your birth date?', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['user_type', 'username', 'first_name', 'last_name', 'email', 'date_of_birth']
