from django.urls import path
# para importars elementos internos uso el .
from . import views

urlpatterns = [
    # Path del core

    path("", views.services, name="services"),
 

]
