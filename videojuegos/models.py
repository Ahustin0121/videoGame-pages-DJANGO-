from django.db import models


class Videojuego(models.Model):
    nombre = models.CharField(max_length=200)
    stock = models.IntegerField()
    consola = models.CharField(max_length=100)
    Estado = models.CharField(max_length=50)
    ano = models.IntegerField()
    PEGI = models.CharField(max_length=10)
    descripcion = models.TextField()
    precio = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='images/videojuegos/', blank=True, null=True)

    def __str__(self):
        return self.nombre