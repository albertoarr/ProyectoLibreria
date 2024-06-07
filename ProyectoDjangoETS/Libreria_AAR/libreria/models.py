from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre + " " + self.apellidos

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    paginas = models.IntegerField(default=0)
    precio = models.FloatField(default=0.00)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default="")


    def __str__(self):
        return self.titulo
