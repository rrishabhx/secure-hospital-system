import random
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
import logging
from django.core.mail import send_mail

from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)


def home(request):
    print("In landing page. Redirecting user to login page")
    return redirect('login-user', usertype='patient')


def about(request):
    return render(request, 'users/about.html')


def login_user(request, usertype):
    print("User trying to login")
    if request.user.is_authenticated:
        print("User authenticated")

        return user_redirect(request)

    if request.method == 'POST':
        print(f"User login POST request: {request.POST}")
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)

            if (usertype == 'patient' and user.user_type != 'patient') or (
                    usertype != 'patient' and user.user_type != request.POST.get('staff')):
                print(f"User-type incorrect! Please login as {user.user_type}")
                messages.error(request, f"User-type incorrect! Please login as {user.user_type}")

                return redirect('login-user', usertype=usertype)
        except:
            messages.error(request, 'User does not exist')
            return redirect('login-user', usertype=usertype)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            print("User type: " + user.user_type)
            messages.success(request, f'{user.username} successfully logged in')
            return user_redirect(request)
        else:
            messages.error(request, 'Username or Password does not exist')

    page = 'patient' if usertype == 'patient' else 'staff'
    return render(request, 'users/login.html', context={'page': page})

global no
no = 0
def otp(request):
    global no
    if request.method == 'POST':
        otp = request.POST.get('otp','')
        if(int(otp)==int(no)):
            return user_redirect(request)
        else:
            u = User.objects.filter(username=u1)
            u.delete()
            return HttpResponse('Invalid OTP.')
    else:
        no=random.randrange(1000,9999)
        send_mail('Your OTP for verification','Your OTP is {}'.format(no),'srivatsavkumar7777@gmail.com',['srivatsavkumar5555@gmail.com'],fail_silently=False)
        return render(request, 'users/otp.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You are now able to log in')
            # login(request, user)

            return redirect('login-user', usertype='patient')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_user(request):
    print("Opening user profile. Redirecting to user-type")

    return user_redirect(request, 'profile')


def user_redirect(request, redirect_page='home'):
    user_type = request.user.user_type

    print(f"Redirecting [{user_type}] to home page: ")

    if user_type == 'patient':
        return redirect(f'patients:{redirect_page}')
    elif user_type == 'doctor':
        return redirect(f'doctors:{redirect_page}')
    elif user_type == 'hospital_staff':
        return redirect(f'hospital_staffs:{redirect_page}')
    elif user_type == 'lab_staff':
        return redirect(f'lab_staffs:{redirect_page}')
    elif user_type == 'insurance_staff':
        return redirect(f'insurance_staffs:{redirect_page}')
    elif user_type == 'administrator':
        return redirect(f'administrators:{redirect_page}')
    else:
        context = {
            'reason': f'Invalid user type: {user_type}'
        }
        response = render(request, context)
        response.status_code = 400
        return response
