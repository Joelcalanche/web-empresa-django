from django.urls import path
# para importars elementos internos uso el .
from . import views


urlpatterns = [
    # Path del core
    
    
    #  escrito asi detectara lo que haya entre las 2 barras(dinamico) y lo enviara a la vista como parametro
    # pero cuidado por que lo enviara como cadena de caracteres, por eso hago el casting a entero
    path("<int:page_id>/<slug:page_slug>",views.page, name="page"),
]


