from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


#MODELOS

class JuegosDePc(models.Model):
    idJuegos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fechaDeLanzamiento = models.DateField()
    genero = models.CharField(max_length=100)
    sinopsis = models.CharField(max_length=200)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de Lanzamiento: {self.fechaDeLanzamiento} - Género: {self.genero} - Sinopsis: {self.sinopsis}"

class JuegosDeConsola(models.Model):
    idJuegosDeConsola = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fechaDeLanzamiento = models.DateField()
    genero = models.CharField(max_length=100)
    consola = models.CharField(max_length=50)
    sinopsis = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de Lanzamiento: {self.fechaDeLanzamiento} - Género: {self.genero} - Consola: {self.consola} - Sinopsis: {self.sinopsis}"

class Noticias(models.Model):
    idNoticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=1500)
    
    def __str__(self):
        return f"Título: {self.titulo} - Subtítulo: {self.subtitulo} - Cuerpo: {self.cuerpo}"

class Avatar(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    imagen = models.ImageField(default='profile1.jpg', upload_to="profile",null=True, blank=True)
    
class Blog(models.Model):
    idBlog = models.AutoField(primary_key=True)    
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField(blank="True", null="True")
    imagen = models.ImageField(upload_to="imagen", null=True, blank=True)
    imagenFecha = models.DateField()
    
    def __str__(self):
        return f"Título: {self.titulo} - Subtítulo: {self.subtitulo} - Cuerpo: {self.cuerpo} - Imagen: {self.imagen} - Fecha Posteo Imagen: {self.imagenFecha}"