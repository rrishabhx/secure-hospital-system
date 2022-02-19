from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

from django.contrib.auth import get_user_model

User = get_user_model()

appointments = [
    {
        'doctor': 'Dr. Mantis Tobbagan',
        'title': 'Covid-19',
        'description': 'No taste in food',
        'date_posted': 'Feb 27, 2022'
    },
    {
        'doctor': 'Dr. Jane Doe',
        'title': 'Cancer',
        'description': 'Too much blood loss',
        'date_posted': 'Feb 18, 2022'
    }
]


def home(request):
    context = {
        'appointments': appointments
    }
    return render(request, 'users/home.html', context)


def about(request):
    return render(request, 'users/about.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('users-home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users-home')
        else:
            messages.error(request, 'Username or Password does not exist')

    context = {}
    return render(request, 'users/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, f'Account created for {user.username}! You are not able to log in')
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_user(request):
    print(f'User type: {request.user.user_type}')
    if request.user.user_type == 'patient':
        return render(request, 'patients/profile.html')

    return render(request, 'users/profile.html')
