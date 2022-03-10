from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin-home'),
    path('test/', views.deleteEmployees, name='delete_employee')
]