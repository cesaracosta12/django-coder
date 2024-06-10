from django.db import models

class Auto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.CharField(max_length=40)
    

class Articulo(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    precio = models.FloatField(max_length=40)