# lbtchat/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_message/', views.send_message, name='send_message'),
]
