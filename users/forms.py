from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class BaseUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

