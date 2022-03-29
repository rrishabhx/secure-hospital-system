from django.contrib import admin
from django.urls import path

from .views import home, get_response, get_bot_response
#
#
# app_name = 'chatbot'

urlpatterns = [
    path('', home, name='home'),
    path('get_response/', get_response, name='get_response'),
    path('get/', get_bot_response,name='get_bot_response')
]
