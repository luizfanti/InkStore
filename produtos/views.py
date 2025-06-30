from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def novo_produto(request):
    if request.method == 'POST':
        Produto.objects.create(
            descricao=request.POST['descricao'],
            preco=request.POST['preco'],
            quantidade=request.POST['quantidade'],
            observacao=request.POST['observacao'],
        )
        return redirect('produtos:lista')
    return render(request, 'produtos/form.html')

def editar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'POST':
        produto.descricao = request.POST['descricao']
        produto.preco = request.POST['preco']
        produto.quantidade = request.POST['quantidade']
        produto.observacao = request.POST['observacao']
        produto.save()
        return redirect('produtos:lista')
    return render(request, 'produtos/form.html', {'produto': produto})

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()
    return redirect('produtos:lista')
