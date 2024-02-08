from django.db import models
# modelo que voy a usar para asignar cada articulo a su usuario
from django.contrib.auth.models import User

# La clase mas importante esta abajo del todo

#   ManyToManyField
class Categoria(models.Model):
    nombre = models.CharField(max_length=20, verbose_name="Nombre de la Categoria")
    descripcion = models.CharField(max_length=100, verbose_name="Descripcion")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación de la categoria")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación de la categoria")

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ["-creado"]



#   BOSS MODEL
class Articulo(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo del articulo")
    texto = models.TextField(verbose_name="Contenido del articulo")
    imagen = models.ImageField(verbose_name="Foto", null=True, blank=True, upload_to="fotos")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del articulo")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación del articulo")
    # Crear un campo para crear una relacion del articulo con el usuario
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # Las categorias a las que pertenece (Solo se pone en uno de los dos modelos)
    categoria = models.ManyToManyField(Categoria, verbose_name="Categoría", )

    # Lo que quiero que salga cuando digo: 'enseñame este objeto'
    def __str__(self):
        return self.titulo
    
    # Cuando pido los objetos: 'como quiero que me los devuelva' (del mas nuevo al mas antiguo) 
    class Meta:
        ordering = ["-creado"]



#   ForeignKey
class Comentario(models.Model):
    texto = models.TextField(verbose_name="Comentario del articulo")
    # pongo articulo para relacionarlo directamennte con la clase de arriba
    #   y añado que se elimine en cascada
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE) 
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación del comentario")
    modificado = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación del comentario")

    def __str__(self):
        return self.texto[:10]+"..." # Para que salgan solo 10 caracteres y '...'
    
    class Meta:
        ordering = ["-creado"]

