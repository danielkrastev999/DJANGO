from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Equipo,Competicion
from django.shortcuts import get_object_or_404
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Equipo, Jugador, Competicion

# Clase inicio que hereda directamente de 'TemplateView'
class inicio(TemplateView):
    template_name = 'principal/inicio.html'

# Ver el contenido de una tabla
class listadoEquipo(ListView):
    model = Equipo

# Ver el contenido de una tabla
class listadoJugadores(ListView):
    model = Jugador

# Ver el contenido de una tabla
class listadoCompeticion(ListView):
    model = Competicion

# Ver los detalles de un equipo en concreto
class detalleEquipo(DetailView):
    model = Equipo

# Ver los detalles de una competicion en concreto
class detalleCompeticion(DetailView):
    model = Competicion

# Ver los detalles de un jugador en concreto
class detalleJugador(DetailView):
    model = Jugador





@method_decorator(login_required,name='dispatch')
class crearEquipo (CreateView):
    # 1. Decir que modelo quiero crear
    model = Equipo
    # 2. Decir los campos que quier mostrar
    fields = ['nombre','categoria','competicion','imagen','responsable']
    # 3. Cuando acabe de crear un equipo que vaya a 'listado'
    success_url = reverse_lazy('listado')

    # 4. Metodo que se ejecuta cuando llegan los datos del form 
    #   Recibe el objeto que se crea en esta clase y el formulario con la info
    def form_valid(self,form):
        # El usuario que esta en el sistema ahora será el que cree en equipo
        form.instance.responsable = self.request.user
        # Este formulario ejecutara la funcion padre de CreateView con el formulario validado !!!!
        return super(crearEquipo,self).form_valid(form)
    

@method_decorator(login_required,name='dispatch')
class borrarEquipo(DeleteView):
    model = Equipo
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Me devuelve el Equipo que se quiere modificar
        equipo = self.get_object()
        
        if equipo.responsable != request.user:
            # Lanza una excepcion de permisos
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    
@method_decorator(login_required,name='dispatch')
class modificarEquipo(UpdateView):
    model = Equipo
    fields = ['nombre','categoria','competicion','responsable']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Me devuelve el Equipo que se quiere modificar
        equipo = self.get_object()

        if equipo.responsable != request.user:
            # Lanza una excepcion de permisos
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)




@method_decorator(login_required,name='dispatch')
class crearJugador (CreateView):
    # 1. Decir que modelo quiero crear
    model = Jugador
    # 2. Decir los campos que quier mostrar
    fields = ['equipo','nombre','correo','imagen','edad']
    # 3. Cuando acabe de crear un equipo que vaya a 'listado'
    success_url = reverse_lazy('listado')

    # 4. Metodo que se ejecuta cuando llegan los datos del form 
    #   Recibe el objeto que se crea en esta clase y el formulario con la info
    def form_valid(self,form):
        # El usuario que esta en el sistema ahora será el que cree en equipo
        form.instance.responsable = self.request.user
        # Este formulario se ejectura con lo que ha heredado de la clase padre (super)
        return super(crearJugador,self).form_valid(form)

@method_decorator(login_required,name='dispatch')
class borrarJugador(DeleteView):
    model = Jugador
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Me devuelve el Equipo que se quiere modificar
        jugador = self.get_object()
        
        if jugador.equipo.responsable != request.user:
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)
    

@method_decorator(login_required,name='dispatch')
class modificarJugador(UpdateView):
    model = Jugador
    fields = ['nombre','correo','edad']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Me devuelve el Equipo que se quiere modificar
        jugador = self.get_object()

        if jugador.equipo.responsable != request.user:
            # Lanza una excepcion de permisos
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


    
@method_decorator(login_required,name='dispatch')
class crearCompeticion (CreateView):
    # 1. Decir que modelo quiero crear
    model = Competicion
    # 2. Decir los campos que quier mostrar
    fields = ['nombre','lugar']
    # 3. Cuando acabe de crear un equipo que vaya a 'listado'
    success_url = reverse_lazy('listado')

    # 4. Metodo que se ejecuta cuando llegan los datos del form 
    #   Recibe el objeto que se crea en esta clase y el formulario con la info
    def form_valid(self,form):
        # El usuario que esta en el sistema ahora será el que cree en equipo
        form.instance.responsable = self.request.user
        # Este formulario se ejectura con lo que ha heredado de la clase padre (super)
        return super(crearCompeticion,self).form_valid(form)
    
@method_decorator(login_required,name='dispatch')
class borrarCompeticion(DeleteView):
    model = Competicion
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Me devuelve el Equipo que se quiere modificar
        competicion = self.get_object()
        
        if competicion.equipo.responsable != request.user:
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required,name='dispatch')
class modificarCompeticion(UpdateView):
    model = Competicion
    fields = ['nombre','correo','edad']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Me devuelve el Equipo que se quiere modificar
        competicion = self.get_object()

        if competicion.equipo.responsable != request.user:
            # Lanza una excepcion de permisos
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
        