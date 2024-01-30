from django.urls import path
from .views import listadoEquipo,detalleEquipo,detalleJugador, detalleCompeticion, crearEquipo, borrarEquipo, modificarEquipo, inicio, listadoCompeticion,borrarCompeticion, modificarCompeticion, listadoJugadores, borrarJugador, modificarJugador, crearJugador,crearCompeticion

urlpatterns = [
    path('', inicio.as_view(),name='inicio'),
    path('listado', listadoEquipo.as_view(),name='listado'),
    path('listar-jugadores', listadoJugadores.as_view(),name='listar-jugadores'),
    path('listar-competicion', listadoCompeticion.as_view(),name='listar-competicion'),

    path('crear-equipo', crearEquipo.as_view(),name='crear_equipo'),
    path('borrar/<int:pk>', borrarEquipo.as_view(),name='borrar'),
    path('modificar/<int:pk>', modificarEquipo.as_view(),name='modificar'),

    path('crear-jugador', crearJugador.as_view(),name='crear_jugador'),
    path('borrar/jugador/<int:pk>/', borrarJugador.as_view(), name='borrar_jugador'),
    path('modificar/jugador/<int:pk>/', modificarJugador.as_view(), name='modificar_jugador'),

    path('crear-competicion', crearCompeticion.as_view(),name='crear_competicion'),
    path('borrar/competicion/<int:pk>/', borrarCompeticion.as_view(), name='borrar_competicion'),
    path('modificar/competicion/<int:pk>/', modificarCompeticion.as_view(), name='modificar_competicion'),

    path('equipo/<int:pk>/', detalleEquipo.as_view(), name='equipo_detail'),
    path('competicion/<int:pk>/', detalleCompeticion.as_view(), name='competicion_detail'),
    path('jugador/<int:pk>/', detalleJugador.as_view(), name='jugador_detail'),

    
]