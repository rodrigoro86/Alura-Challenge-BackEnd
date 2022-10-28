from enum import unique
from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    url = models.CharField(max_length=300, unique=True)

    def __str__(self) -> str:
        return self.nome

