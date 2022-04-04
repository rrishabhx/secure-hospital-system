from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/', views.appointments, name='appointments'),
    path('diagnosis/', views.diagnosis, name='diagnosis'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('lab_test_reports/', views.lab_test_reports, name='lab-test-reports'),
    path('insurance/', views.insurance, name='insurance'),
    path('transactions/', views.transactions, name='transactions'),
    path('verify/<str:hfunc>', views.verify_patient, name='verify-patient'),
    path('profile/', views.profile, name='profile'),
    path('requestPolicy/', views.requestPolicy, name='requestPolicy'),
    path('receipt/', views.receipt, name='receipt')
]
