from ast import Pass
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.

class VRegistro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()   # Graba la info del formulario en la base de datos
            login(request, usuario)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,"registro/registro.html",{"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

class VLogin(View):
    def get(self, request):
        form=AuthenticationForm()
        return render(request,"login/login.html",{"form":form})

    def post(self,request):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información Incorrecta")
        return render(request,"login/login.html",{"form":form})


class VCambiarContraseña(View):
    def get(self, request):
        form=PasswordChangeForm(user=request.user)
        return render(request,"change/change.html",{"form":form})

    def post(self,request):
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            nombre_usuario=form.cleaned_data.get("username")
            contra = form.cleaned_data.get("newpassword")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                return redirect('login')
        else:
            messages.error(request, "Información Incorrecta")
            return render(request,"change/change.html",{"form":form})
