from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['user_type', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']
