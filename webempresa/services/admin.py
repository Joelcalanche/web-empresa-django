from django.contrib import admin

from .models import Service

# para que que el modelo este disponible para el admministrador debemos importadlo
# Register your models here.

# una vez importado el modelo crearemos una configuracion basica

class ServiceAdmin(admin.ModelAdmin):

    # campos de solo lectura
    readonly_field =('created','update')



# Registrado el modelo y su configuracion
admin.site.register(Service, ServiceAdmin)
