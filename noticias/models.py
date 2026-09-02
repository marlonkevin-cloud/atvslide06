from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

def __str__(self):
    return self.nome

class Tag(models.Model):
    titulo = models.CharField(max_length=100)

def __str__(self):
    return self.titulo

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="noticias")
    tags = models.ManyToManyField(Tag)

def __str__(self):
    return self.titulo

class Perfil(models.Model):
    Bio = models.CharField(max_length=100)
    user = models.OneToOneField(Usuario)
