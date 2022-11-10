from django.db import models

# Create your models here.
class Excursiones(models.Model):
      nombre = models.CharField(max_length=100)
      descripcion = models.CharField(max_length=3000)
      precio = models.IntegerField()
      #date_published = models.DateTimeField(auto_now_add=True)
      imagen = models.ImageField(upload_to="paisaje", null=True, blank=True)

def __str__(self):
      return f"id:{self.id},Nombre: {self.nombre}, -Descripción: {self.descripcion}, Precio: {self.precio} , {self.imagen}"