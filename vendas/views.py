from django.shortcuts import render, redirect, get_object_or_404
from .models import Venda, ItemVenda
from clientes.models import Cliente
from funcionarios.models import Funcionario
from produtos.models import Produto

def lista_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/lista.html', {'vendas': vendas})

def nova_venda(request):
    clientes = Cliente.objects.all()
    funcionarios = Funcionario.objects.all()
    produtos = Produto.objects.all()

    if request.method == 'POST':
        venda = Venda.objects.create(
            cliente_id=request.POST['cliente'],
            funcionario_id=request.POST['funcionario']
        )

        for i in range(len(request.POST.getlist('produto'))):
            ItemVenda.objects.create(
                venda=venda,
                produto_id=request.POST.getlist('produto')[i],
                quantidade=request.POST.getlist('quantidade')[i],
                preco=request.POST.getlist('preco')[i]
            )
        return redirect('vendas:lista')

    return render(request, 'vendas/form.html', {
        'clientes': clientes,
        'funcionarios': funcionarios,
        'produtos': produtos
    })

def excluir_venda(request, id):
    venda = get_object_or_404(Venda, pk=id)
    venda.delete()
    return redirect('vendas:lista')
