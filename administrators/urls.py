from django.urls import path
from . import views

app_name = 'administrators'

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.base, name='base'),
    path('create/', views.create, name='create'),
    path('fetch/', views.fetch, name='fetch'),
    path('modify/', views.modify, name='modify'),
    path('saveModify/', views.saveModify, name='saveModify'),
    path('delete/', views.delete, name='delete'),
    path('confirmDelete/', views.confirmDelete, name='confirmDelete'),
    path('save_modify/', views.save_modify, name='save_modify'),
    path('transactions/', views.transactions, name='transactions'),
]
