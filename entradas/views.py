from django.shortcuts import render, redirect, get_object_or_404
from .models import Entrada, ItemEntrada
from fornecedores.models import Fornecedor
from produtos.models import Produto

def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'entradas/lista.html', {'entradas': entradas})

def nova_entrada(request):
    fornecedores = Fornecedor.objects.all()
    produtos = Produto.objects.all()

    if request.method == 'POST':
        entrada = Entrada.objects.create(
            fornecedor_id=request.POST['fornecedor']
        )
        for i in range(len(request.POST.getlist('produto'))):
            ItemEntrada.objects.create(
                entrada=entrada,
                produto_id=request.POST.getlist('produto')[i],
                quantidade=request.POST.getlist('quantidade')[i],
                preco=request.POST.getlist('preco')[i]
            )
        return redirect('entradas:lista')

    return render(request, 'entradas/form.html', {
        'fornecedores': fornecedores,
        'produtos': produtos
    })

def excluir_entrada(request, id):
    entrada = get_object_or_404(Entrada, pk=id)
    entrada.delete()
    return redirect('entradas:lista')
