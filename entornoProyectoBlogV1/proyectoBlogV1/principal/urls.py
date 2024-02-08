from django.urls import path
from . import views

urlpatterns  = [
    path('articulos/',views.listadoArticulo,name='listado'),
    path('categoria/<int:categ_id>/', views.articulosXcategoria, name='artxcatg')
]
