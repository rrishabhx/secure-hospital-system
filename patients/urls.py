from django.urls import path
from . import views

app_name = "patients"

urlpatterns = [
    path('', views.home, name='patient-home'),
    path('appointments', views.appointments, name='appointments'),
    path('diagnosis', views.diagnosis, name='diagnosis'),
    path('prescriptions', views.prescriptions, name='prescriptions'),
    path('reports', views.reports, name='reports'),
    path('insurance', views.insurance, name='insurance'),
    path('transactions', views.transactions, name='transactions'),
    path('profile', views.profile, name='profile')
]
