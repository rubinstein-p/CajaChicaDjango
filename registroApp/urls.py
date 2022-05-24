from django.urls import path, include
from .views import VRegistro,VLogin

urlpatterns = [
    path('register/', VRegistro.as_view(), name='register'),
    path('login/', VLogin.as_view(),  name='login'),
]