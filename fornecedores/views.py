from django.shortcuts import render, redirect, get_object_or_404
from .models import Fornecedor
from cidades.models import Cidade

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/lista.html', {'fornecedores': fornecedores})

def novo_fornecedor(request):
    cidades = Cidade.objects.all()
    if request.method == 'POST':
        Fornecedor.objects.create(
            nome=request.POST['nome'],
            cnpj=request.POST['cnpj'],
            telefone=request.POST['telefone'],
            endereco=request.POST['endereco'],
            numero=request.POST['numero'],
            bairro=request.POST['bairro'],
            email=request.POST['email'],
            cidade_id=request.POST['cidade'],
        )
        return redirect('fornecedores:lista')
    return render(request, 'fornecedores/form.html', {'cidades': cidades})

def editar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, pk=id)
    cidades = Cidade.objects.all()
    if request.method == 'POST':
        fornecedor.nome = request.POST['nome']
        fornecedor.cnpj = request.POST['cnpj']
        fornecedor.telefone = request.POST['telefone']
        fornecedor.endereco = request.POST['endereco']
        fornecedor.numero = request.POST['numero']
        fornecedor.bairro = request.POST['bairro']
        fornecedor.email = request.POST['email']
        fornecedor.cidade_id = request.POST['cidade']
        fornecedor.save()
        return redirect('fornecedores:lista')
    return render(request, 'fornecedores/form.html', {'fornecedor': fornecedor, 'cidades': cidades})

def excluir_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, pk=id)
    fornecedor.delete()
    return redirect('fornecedores:lista')
