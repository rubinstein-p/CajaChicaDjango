from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Vregister, name='register'),
    #  path('login/', views.Vlogin,  name='login'),
]