from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from .views import VRegistro, cerrar_sesion, VLogin, VCambiarContraseña


urlpatterns = [
    path('registro/', VRegistro.as_view() , name="registro" ),
    path('', cerrar_sesion , name="cerrar_sesion" ),
    path('login/', VLogin.as_view() , name="login" ),
    path('cambiar/', VCambiarContraseña.as_view() , name="cambiar" ),
]    