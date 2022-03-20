from django.urls import path
from . import views

app_name = 'hospital_staffs'

urlpatterns = [
    path('', views.home, name='home'),
]