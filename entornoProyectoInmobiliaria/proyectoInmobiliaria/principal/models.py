from django.db import models

# Create your models here.
class Piso(models.Model):
    # Crear los campos del modelo, un campo corresponde con una columna de la tabla 'principal_piso'
    numReferencia = models.CharField(max_length=200,unique=True)
    imagenPiso = models.ImageField(verbose_name="Imagen de piso", null=True, blank=True, upload_to="imgPisos")
    direccion = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=80)
    cp = models.CharField(max_length=10)
    precio = models.FloatField()
    metrosCuadrados = models.IntegerField()
    numHabitantes = models.IntegerField()
    planta = models.IntegerField()
    banios = models.IntegerField()
    ascensor = models.BooleanField()
    garaje = models.BooleanField()
    terraza = models.BooleanField()
    descCorta = models.CharField(max_length=200)
    comentario = models.TextField()
    correoContacto = models.EmailField()
    fechaAlta = models.DateField(auto_now_add=True,verbose_name="Fecha de alta")
    fechaModificacion = models.DateField(auto_now=True, verbose_name="Fecha de modificación")

    # Cuando llamas a la clase Piso, te devuelve el numero de referencia solo
    def __str__(self):
        return self.numReferencia +" ("+self.poblacion+")"
    
    # Cada vez que pida una lista de pisos, que me lo ordene por 'cp'
    # si no pones nada, lo ordena por 'id'
    class Meta:
        ordering = ["poblacion","cp"]

# Modelo de cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField()
    inversor = models.BooleanField()

    def __str__(self):
        return self.nombre + " " + self.apellido