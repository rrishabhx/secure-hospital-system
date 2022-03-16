from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, PatientProfileUpdateForm
import logging

from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)

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
    print("In home page")
    return redirect('login')


def about(request):
    return render(request, 'users/about.html')


def login(request):
    page = 'login'

    print(request)
    if request.user.is_authenticated:
        print("User is authenticated")

        return user_redirect(request)

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login(request)
            # login(request, user)

            # print("User type: " + user.user_type)

            return user_redirect(request)
        else:
            messages.error(request, 'Username or Password does not exist')

    context = {'page': page}
    return render(request, 'users/login.html', context=context)


# def login_staff(request):
#     page = 'login-staff'

#     print(request)
#     if request.user.is_authenticated:
#         print("User is authenticated")

#         return user_redirect(request)

#     if request.method == 'POST':
#         username = request.POST.get('username').lower()
#         password = request.POST.get('password')
#         staff = request.POST.get('staff')

#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'User does not exist')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)

#             print("User type: " + user.user_type)

#             return user_redirect(request)
#         else:
#             messages.error(request, 'Username or Password does not exist')

#     context = {'page': page}
#     return render(request, 'users/login_staff.html', context=context)


# def login_patient(request):
#     page = 'login-patient'

#     print(request)
#     if request.user.is_authenticated:
#         print("User is authenticated")

#         return user_redirect(request)

#     if request.method == 'POST':
#         username = request.POST.get('username').lower()
#         password = request.POST.get('password')

#         try:
#             user = User.objects.get(username=username)
#         except:
#             messages.error(request, 'User does not exist')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)

#             print("User type: " + user.user_type)

#             return user_redirect(request)
#         else:
#             messages.error(request, 'Username or Password does not exist')

#     context = {'page': page}
#     return render(request, 'users/login_patient.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(f"Register form data: {form}")

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! You are now able to log in')
            # login(request, user)

            return redirect('login-patient')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile_user(request):
    logger.info("Inside user profile")

    if request.method == 'POST':
        logger.info("Request type: POST")
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PatientProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.patientprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        logger.info(f"Request type: GET")
        u_form = UserUpdateForm(instance=request.user)
        p_form = PatientProfileUpdateForm(instance=request.user.patientprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    if request.user.user_type == 'patient':
        logger.info("User type: Patient")
        return render(request, 'patients/profile.html', context)

    return render(request, 'users/profile.html')


def user_redirect(request):
    utype = request.user.user_type

    print(f"Redirecting [{utype}] to home page: ")

    if utype == 'patient':
        return redirect('patient-home')
    elif utype == 'doctor':
        return redirect('doctor-home')
    elif utype == 'hospital_staff':
        return redirect('hospitalstaff-home')
    elif utype == 'lab_staff':
        return redirect('labstaff-home')
    elif utype == 'insurance_staff':
        return redirect('insurancestaff-home')
    else:
        context = {
            'reason': f'Invalid user type: {utype}'
        }
        response = render(request, context)
        response.status_code = 400
        return response
