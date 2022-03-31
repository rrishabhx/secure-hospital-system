from django.urls import path
from . import views

app_name = 'administrators'

urlpatterns = [
    path('', views.base, name='home'),
    path('home/', views.base, name='home'),
    path('transactions/', views.transactions, name='transactions'),
    path('employees/', views.employees, name='employees'),
    path('employees/<str:username>/', views.employees_detail, name='employees-detail'),
    path('profile/', views.profile, name='profile'),
    path('log/', views.log, name='log')
]
