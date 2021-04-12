from django.shortcuts import render
from .models import Service
# Create your views here.



def services(request):

    #generaremos los servicios dinamicamente

    services = Service.objects.all()
    
    return render(request,"services/services.html",{'services':services})