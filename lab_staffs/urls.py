from django.urls import path
from . import views

app_name = 'lab_staffs'

urlpatterns = [
    path('', views.home, name='labstaff-home'),
    path('viewdiagnosis/', views.viewDiagnosis, name='viewDiagnosis'),
    path('viewdiagnosis/approveordeny/', views.approve_or_deny, name='approve_deny'),
    path('createreport/', views.createReport, name='createReport'),
    path('deleteandupdatereport/', views.deleteAndUpdateReport, name='deleteAndUpdateReport'),
    path('viewreport/', views.viewReport, name='viewReport'),
    path('updatereport/<int:id>', views.updateReport, name='updateReport'),
    path('', views.home, name='home'),
]