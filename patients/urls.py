from django.urls import path
from . import views

app_name = "patients"

urlpatterns = [
    path('', views.home, name='patient-home'),
    path('appointments', views.appointments, name='appointments'),
    # path('', name='diagnosis'),
    # path('', name='prescriptions'),
    # path('', name='reports'),
    path('insurance', views.insurance, name='insurance'),
    # path('', name='transactions'),
    path('profile', views.profile, name='profile')
]
