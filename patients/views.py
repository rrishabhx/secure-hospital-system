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


# Create your views here.
def home(request):
    context = {
        'appointments': appointments
    }
    return render(request, 'patients/home.html', context)
