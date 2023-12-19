from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Piso,Cliente

# Create your views here.
def catalogo(request):
    catalogo = loader.get_template('principal/catalogo.html')

    # Hacer una consulta a bbdd de todos los pisos (SELECT * FROM piso)
    #   Piso.objects.all()

    contexto = {
        'pisos':Piso.objects.all(), # Django en vez de usar selects, uso la capa ORM (objetos)
        # Lo que traigo lo asocio a 'pisos' y luego lo recorro en 'catalogo.html' con un for para mostrar los datos
        'clientes':Cliente.objects.all(),
    }

    return HttpResponse(catalogo.render(contexto,request))

# Crear un cliente
def crearCliente(request):
    # Insertar un cliente
    cli = Cliente(nombre="El Pepe",apellido="Fernandez", telefono="643234564", correo="elpepe@gmail.com", inversor=False)
    # Guardar el cliente
    cli.save()
    # Para ejecutarlo, tenemos que añadirlo a urls.py
    # Para volver a llamar a 'catalogo' hay que importar 'HttpResponseRedirect' y 'reverse'
    return HttpResponseRedirect(reverse('catalogo'))

# Modificar un cliente
def modificarCliente(request):
    # Acceder a un cliente concreto por el 'id'
    # el metodo 'get' devuelve solo 1 registro, es obligatorio que sea asi
    cli = Cliente.objects.get(id=1) 
    # Modificar un campo de ese cliente
    cli.telefono="611111111"
    # Guardar el cambio
    cli.save()
    # Para volver a llamar a 'catalogo' hay que importar 'HttpResponseRedirect' y 'reverse'
    return HttpResponseRedirect(reverse('catalogo'))

# Borrar un cliente
def borrarCliente(request):
    # Acceder a un cliente concreto por el 'id'
    # el metodo 'get' devuelve solo 1 registro, es obligatorio que sea asi
    try:
        cli = Cliente.objects.get(id=4) 
        # Confirmar la eliminacion 
        cli.delete()
    except:
        pass
    # Para volver a llamar a 'catalogo' hay que importar 'HttpResponseRedirect' y 'reverse'
    return HttpResponseRedirect(reverse('catalogo'))