from django.contrib import admin
from .models import Equipo, Jugador, Competicion

class EquipoAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","categoria","creado","modificado")

class JugadorAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","correo","edad","creado","modificado")

class CompeticionAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","lugar","creado","modificado")


# Register your models here.
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Competicion, CompeticionAdmin)