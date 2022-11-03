from enum import unique
from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    url = models.CharField(max_length=300, unique=True)

    def __str__(self) -> str:
        return self.nome

class Categoria(models.Model):
    titulo = models.CharField(max_length=30)
    cor = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.titulo