from django.db import models
# modelo que voy a usar para asignar cada articulo a su usuario
from django.contrib.auth.models import User

# Create your models here.

#   ManyToManyField
class Competicion(models.Model):
    nombre = models.CharField(max_length=20, verbose_name="Nombre de la Competicion")
    lugar = models.CharField(max_length=50, verbose_name="Lugar")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación de la competicion")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación de la competicion")

    def __str__(self):
        return self.nombre
    
    class Meta:
        pass


class Equipo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre del Equipo")
    categoria = models.CharField(max_length=50, verbose_name="Categoria")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del Equipo")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación del Equipo")
    competicion = models.ManyToManyField(Competicion, verbose_name="Competicion")
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)

    # Lo que quiero que salga cuando digo: 'enseñame este objeto'
    def __str__(self):
        return self.nombre
    
    # Cuando pido los objetos: 'como quiero que me los devuelva' (del mas nuevo al mas antiguo) 
    class Meta:
        pass



class Jugador(models.Model):
    # pongo equipo para relacionarlo directamennte con la clase de arriba
    #   y añado que se elimine en cascada
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=50,verbose_name="Nombre del Jufador")
    correo = models.EmailField()
    imagen = models.ImageField(verbose_name="Foto", null=True, blank=True, upload_to="fotos")
    edad = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del comentario")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación del comentario")

    def __str__(self):
        return self.nombre 
    
    class Meta:
        pass