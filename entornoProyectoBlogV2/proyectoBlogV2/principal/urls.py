from django.urls import path
from .views import inicio, listadoArticulos, crearArticulo, borrarArticulo, modificarArticulo

urlpatterns = [
    # Llamamos al metodo as_view() -> me presenta un formulario y se crea en la bd al darle a crear
    #   as_view() llama al metodo dispatch() -> Realiza un analisis de la peticion
    path('', inicio.as_view(),name='inicio'),
    path('listado', listadoArticulos.as_view(),name='listado'),
    path('crear', crearArticulo.as_view(),name='crear'),
    path('borrar/<int:pk>', borrarArticulo.as_view(),name='borrar'),
    path('modificar/<int:pk>', modificarArticulo.as_view(),name='modificar'),
]