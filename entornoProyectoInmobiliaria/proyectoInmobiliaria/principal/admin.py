from django.contrib import admin
from .models import Piso, Cliente

# Clases para configurar el interfaz de administracion
class PisoAdmin(admin.ModelAdmin):
    list_display = ("numReferencia","poblacion","direccion","precio","fechaAlta","fechaModificacion")
    # Filtrado
    list_filter = ("poblacion","cp")
    # Busquedas
    search_fields = ("poblacion",)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","telefono","correo","inversor")
    search_fields = ("nombre",)



# Registro de modelos
admin.site.register(Piso, PisoAdmin)
admin.site.register(Cliente, ClienteAdmin)