import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from secure_hospital_system import settings
from .forms import UserRegisterForm, CodeForm

User = get_user_model()
logger = logging.getLogger(__name__)


def home(request):
    print("In landing page. Redirecting user to login page")
    return redirect('login-user', usertype='patient')


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
            print(
                f"usertype:{usertype}, user_type:{user.user_type}, request.POST.get_staff:{request.POST.get('staff')}")

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
            # request.session['pk'] = user.pk
            # return redirect('verify-user', usertype=usertype)

            login(request, user)

            print("User type: " + user.user_type)
            messages.success(request, f'{user.username} successfully logged in')
            return user_redirect(request)
        else:
            messages.error(request, 'Username or Password does not exist')

    page = 'patient' if usertype == 'patient' else 'staff'
    return render(request, 'users/login.html', context={'page': page})


def verify_user(request, usertype):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')

    if pk:
        user = User.objects.get(pk=pk)
        code = user.code
        code_user = f"{user.username}: {user.code}"

        if not request.POST:
            # send email
            send_otp_through_email(user, code)
            print(code_user)

        if form.is_valid():
            num = form.cleaned_data.get('number')

            if str(code) == num:
                code.save()
                login(request, user)

                messages.success(request, f'{user.username} successfully logged in')
                return user_redirect(request)
            else:
                messages.error(request, f'Incorrect OTP!! Please try again.')
                return redirect('login-user', usertype=usertype)

    return render(request, 'users/verify.html', {'form': form})


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


def send_otp_through_email(user, otp):
    try:
        send_mail(subject="Dr. Yau's Clinic Email Verification Code", message=f"OTP: {otp}",
                  from_email=settings.EMAIL_HOST_USER, recipient_list=[user.email])
    except:
        print(f"Exception occurred while sending OTP to {user.username}: {user.email}")
