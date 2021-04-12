from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'

    # si queremos traducir agregramos un verbose

    verbose_name ='Gestor de servicios'
