from django.urls import path
from . import views

app_name = 'insurance_staffs'

urlpatterns = [
    path('', views.home, name='home'),
    path('claims/', views.claims, name='claims'),
    path('policies/', views.policies, name='policies'),
    path('profile/', views.profile, name='profile')
]
