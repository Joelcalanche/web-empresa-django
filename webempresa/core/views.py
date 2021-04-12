from django.shortcuts import render, HttpResponse

# Create your views here.

# Inicio home/
# Historia about/
# Servicios services/
# Visitanos store/
# Contacto contact/
# Blog blog/
# Sample sample/
# el HttpResponse solo lo usamos al inicio

def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

# def services(request):

#     return render(request,"core/services.html")

def store(request):
    return render(request,"core/store.html")

# def contact(request):
#     return render(request,"core/contact.html")

# def blog(request):
#     return render(request,"core/blog.html")

# def sample(resquest):
#     return render(resquest,"core/sample.html")