from django.shortcuts import render
from cajachicaApp.models import Habilitocajachica, Sectores

# Create your views here.

def home(request):
    cajashabilitadas = Habilitocajachica.objects.all()
    sectores = Sectores.objects.all()
    return render(request,'cajachicaApp/home.html',{"cajashabilitadas":cajashabilitadas,"sectores":sectores})