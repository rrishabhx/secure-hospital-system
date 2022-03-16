from django.contrib.auth.decorators import login_required

from hospital.forms import AppointmentCreationForm
from users.decorators import patient_required
from django.shortcuts import render
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


# @login_required
# @patient_required
def home(request):
    appointment_form = AppointmentCreationForm()

    context = {
        'appointments': appointments,
        'appointment_form': appointment_form
    }

    return render(request, 'patients/home.html', context)


def appointments(request):
    return render(request,'patients/appointments.html')

def diagnosis(request):
    pass

def prescriptions(request):
    pass

def reports(request):
    pass

def insurance(request):
    pass

def transactions(request):
    pass

def profile(request):
    pass