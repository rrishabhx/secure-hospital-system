from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hospitalstaff-home'),
    path('createPatient', views.createPatient, name='hospitalstaff-createPatient'),
    path('viewPatient', views.viewPatient, name='hospitalstaff-viewPatient'),
    path('viewRecords', views.viewRecords, name='hospitalstaff-viewRecords'),
    path('viewLabRecords', views.viewLabTests, name='hospitalstaff-viewLabRecords'),
    path('createTransaction', views.createTransaction, name='hospitalstaff-createTransaction'),
]