from django.urls import path
from . import views

app_name = 'lab_staffs'

urlpatterns = [
    path('', views.home, name='home'),
]