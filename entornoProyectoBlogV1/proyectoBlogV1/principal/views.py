from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Articulo,Categoria
from django.shortcuts import get_object_or_404

# Create your views here.
def listadoArticulo(request):
    # Traer de la BD todos los articulos
    articulos = Articulo.objects.all()  
    # Django utiliza un ORM donde en vez de usar selects, uso la capa ORM (objetos)

    # Crear un contexto para renderizar la plantilla
    contexto = {
        'articulos' : articulos,
    }
    # Cargar la plantilla
    listado = loader.get_template('principal/listado.html')

    # Devolver el httpResponse con la plantilla renderizada
    return HttpResponse(listado.render(contexto,request))



def articulosXcategoria(request,categ_id):
    # Recuperar los articulos de la categoria categ_id
    #  Traer solo UNA categoria
    # categoria = Categoria.objects.get(id=categ_id)
    categoria = get_object_or_404(Categoria,id=categ_id)

    return render(request,'principal/listado.html',{
        'nombreCateg': categoria.nombre,
        'articulos' : categoria.articulo_set.all()
    })