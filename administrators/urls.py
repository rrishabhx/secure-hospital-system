from django.urls import path
from . import views

app_name = 'administrators'

urlpatterns = [
    path('', views.base, name='home'),
    path('home/', views.base, name='home'),
    # path('create/', views.create, name='create'),
    # path('fetch/', views.fetch, name='fetch'),
    # path('modify/', views.modify, name='modify'),
    # path('saveModify/', views.saveModify, name='saveModify'),
    # path('delete/', views.delete, name='delete'),
    # path('confirmDelete/', views.confirmDelete, name='confirmDelete'),
    # path('save_modify/', views.save_modify, name='save_modify'),
    path('transactions/', views.transactions, name='transactions'),
    path('employees/', views.employees, name='employees'),
    path('employees/<str:username>/', views.employees_detail, name='employees-detail'),
    path('profile/', views.profile, name='profile'),
    path('log/', views.log, name='log')
]
