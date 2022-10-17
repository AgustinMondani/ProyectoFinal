from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models


class Autor(models.Model):
    class Meta:
        verbose_name_plural = ("Autores")

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    especialidad = models.CharField(max_length=40)

    def __str__(self) :
        return f"{self.nombre} {self.apellido}"  # para que aparezca mas bonito en el administrador


class Articulo(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.CharField(max_length=350)
    fecha = models.DateField(null=True)

    def __str__(self) :
        return self.titulo # para que aparezca mas bonito en el administrador


class Seccion(models.Model):
    class Meta:
        verbose_name_plural = ("Secciones")

    nombre = models.CharField(max_length=30)

    def __str__(self) :
        return self.nombre  # para que aparezca mas bonito en el administrador
