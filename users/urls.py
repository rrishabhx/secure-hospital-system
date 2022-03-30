from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'users'

urlpatterns = [
    path('', views.home, name='users-home'),
    path('about/', views.about, name='users-about'),  # delete this route
    path('login/<str:usertype>', views.login_user, name='login-user'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile_user, name='profile'),
    path('otp/',views.otp, name='otp')
]
