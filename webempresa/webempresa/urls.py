"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# Inicio home/
# Historia about/
# Servicios services/
# Visitanos store/
# Contacto contact/
# Blog blog/
# Sample sample/





urlpatterns = [
    # Path del core
    path('', include('core.urls')),
    # Path de de la app services
    path('services/', include('services.urls')),

    # path de la app blog
    path('blog/', include('blog.urls')),

    # path de la app pages
    path('page/', include('pages.urls')),

    # path de la contact pages
    path('contact/', include('contact.urls')),


    # Path del admin
    path('admin/', admin.site.urls),
]

# para poder servir media
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)