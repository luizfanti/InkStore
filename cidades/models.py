from django.db import models
from estados.models import Estado

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.estado.sigla}"
