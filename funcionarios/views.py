from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionario
from cidades.models import Cidade

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios/lista.html', {'funcionarios': funcionarios})

def novo_funcionario(request):
    cidades = Cidade.objects.all()
    if request.method == 'POST':
        Funcionario.objects.create(
            nome=request.POST['nome'],
            cpf=request.POST['cpf'],
            telefone=request.POST['telefone'],
            endereco=request.POST['endereco'],
            numero=request.POST['numero'],
            bairro=request.POST['bairro'],
            email=request.POST['email'],
            senha=request.POST['senha'],
            cidade_id=request.POST['cidade'],
        )
        return redirect('funcionarios:lista')
    return render(request, 'funcionarios/form.html', {'cidades': cidades})

def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    cidades = Cidade.objects.all()
    if request.method == 'POST':
        funcionario.nome = request.POST['nome']
        funcionario.cpf = request.POST['cpf']
        funcionario.telefone = request.POST['telefone']
        funcionario.endereco = request.POST['endereco']
        funcionario.numero = request.POST['numero']
        funcionario.bairro = request.POST['bairro']
        funcionario.email = request.POST['email']
        funcionario.senha = request.POST['senha']
        funcionario.cidade_id = request.POST['cidade']
        funcionario.save()
        return redirect('funcionarios:lista')
    return render(request, 'funcionarios/form.html', {'funcionario': funcionario, 'cidades': cidades})

def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    funcionario.delete()
    return redirect('funcionarios:lista')
