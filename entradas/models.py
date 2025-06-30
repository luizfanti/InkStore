# entradas/models.py
from django.db import models
from fornecedores.models import Fornecedor
from produtos.models import Produto

class Entrada(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    dataEntrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrada #{self.id} - {self.dataEntrada.strftime('%d/%m/%Y')}"

class ItemEntrada(models.Model):
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.descricao}"
