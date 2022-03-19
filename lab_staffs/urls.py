from django.urls import path
from . import views

app_name = 'lab_staffs'

urlpatterns = [
    path('', views.home, name='labstaff-home'),
    path('viewdiagnosis/', views.viewDiagnosis, name='viewDiagnosis'),
    path('createreport/', views.createReport, name='createReport'),
    path('deletereport/', views.deleteReport, name='deleteReport'),
    path('updatereport/', views.updateReport, name='updateReport'),
    path('', views.home, name='home'),
]