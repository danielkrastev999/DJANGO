"""
URL configuration for proyectoInmobiliaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
# importamos static manualmente (en la ayuda de vs no aparece)
from django.conf.urls.static import static
from principal import views

urlpatterns = [
    # Cuando entre dentro de la ruta vacia, que se vaya a buscar el metodo 'catalogo' dentro de views.py
    path('',views.catalogo,name='catalogo'),
    path('crearCliente/',views.crearCliente,name='crearCliente'),
    path('modificarCliente/',views.modificarCliente, name='modificarCliente'),
    path('borrarCliente/',views.borrarCliente, name='borrarCliente'),
    path('borrarPepes/',views.borrarPepe, name='borrarPepes'),
    
    path('admin/', admin.site.urls),
]

# Si el modo debug esta activada le añadimos al 'urlpatterns' 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Añado algo que se ejecuta con static, que le da una ruta y le dice que hacer con ella
    # Los ficheros static son el css, las imagenes, js etc