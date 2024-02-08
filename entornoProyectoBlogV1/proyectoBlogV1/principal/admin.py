from django.contrib import admin
from .models import Articulo, Comentario, Categoria

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("id","titulo","texto","imagen","creado","modificado")

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("id","texto","articulo","creado","modificado")

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","descripcion","creado","modificado")


# Register your models here.
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Categoria, CategoriaAdmin)