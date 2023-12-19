from django.http import HttpResponse
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