from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length=2000)

class Autor(models.Model):
    nombre_autor = models.CharField(max_length=40)
    nacionalidad_autor = models.CharField(max_length=40)

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=40)
   


