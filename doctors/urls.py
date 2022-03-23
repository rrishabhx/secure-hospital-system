from django.urls import path
from . import views

app_name = "doctors"

urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/', views.appointments, name='appointments'),
    path('diagnosis/', views.diagnosis, name='diagnosis'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('reports/', views.reports, name='reports'),
    path('profile/', views.profile, name='profile')
]