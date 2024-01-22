from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Articulo

# Clase inicio que hereda directamente de 'TemplateView'
class inicio(TemplateView):
    template_name = 'principal/inicio.html'

# Ver el contenido de una tabla
class listadoArticulos(ListView):
    model = Articulo


@method_decorator(login_required,name='dispatch')
class crearArticulo (CreateView):
    # 1. Decir que modelo quiero crear
    model = Articulo
    # 2. Decir los campos que quier mostrar
    fields = ['titulo','texto','imagen','categorias','autor']
    # 3. Cuando acabe de crear un articulo que vaya a 'listado'
    success_url = reverse_lazy('listado')

    # 4. Metodo que se ejecuta cuando llegan los datos del form 
    #   Recibe el objeto que se crea en esta clase y el formulario con la info
    def form_valid(self,form):
        # El usuario que esta en el sistema ahora será el que cree el articulo
        form.instance.autor = self.request.user
        # Este formulario se ejectura con lo que ha heredado de la clase padre (super)
        return super(crearArticulo,self).form_valid(form)
    
@method_decorator(login_required,name='dispatch')
class borrarArticulo(DeleteView):
    model = Articulo
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Me devuelve el articulo que se quiere modificar
        articulo = self.get_object()
        
        if articulo.autor != request.user:
            # Lanza una excepcion de permisos
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required,name='dispatch')
class modificarArticulo(UpdateView):
    model = Articulo
    fields = ['texto','imagen','categorias']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('listado')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        # Me devuelve el articulo que se quiere modificar
        articulo = self.get_object()

        if articulo.autor != request.user:
            # Lanza una excepcion de permisos
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
