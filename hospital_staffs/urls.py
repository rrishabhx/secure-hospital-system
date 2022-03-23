from django.urls import path
from . import views

app_name = 'hospital_staffs'

urlpatterns = [
    path('', views.home, name='home'),
    path('createPatient/', views.createPatient, name='createPatient'),
    path('viewPatient/', views.viewPatient, name='viewPatient'),
    path('viewRecords/', views.viewRecords, name='viewRecords'),
    path('viewLabRecords/', views.viewLabTests, name='viewLabRecords'),
    path('createTransaction/', views.createTransaction, name='createTransaction'),
    path('approveTransaction/', views.approveTransaction, name='approveTransaction'),
    path('approveAppointment/', views.approveAppointment, name='approveAppointment'),
]