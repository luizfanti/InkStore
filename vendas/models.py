# vendas/models.py
from django.db import models
from clientes.models import Cliente
from funcionarios.models import Funcionario
from produtos.models import Produto

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    dataVenda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda #{self.id} - {self.dataVenda.strftime('%d/%m/%Y')}"

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.descricao}"

