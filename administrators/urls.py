from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin-home'),
    path('delete/', views.deleteEmployees, name='delete_employee'),
    path('modify/', views.getEmployee, name='get_employee'),
    path('save_modify/', views.save_modify, name='save-modify')
]