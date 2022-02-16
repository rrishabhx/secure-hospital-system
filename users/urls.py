from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='users-home'),
    path('about/', views.about, name='users-about'),  # delete this route
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile_user, name='profile'),
]
