from django.urls import path
# para importars elementos internos uso el .
from . import views

urlpatterns = [
    # Path del contact

    path("", views.contact, name="contact"),



]
