from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from cidades.models import Cidade

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})

def novo_cliente(request):
    cidades = Cidade.objects.all()
    if request.method == 'POST':
        try:
            cidade_id = int(request.POST.get('cidade'))
            cliente = Cliente(
                nome=request.POST['nome'],
                cpf=request.POST['cpf'],
                telefone=request.POST['telefone'],
                endereco=request.POST['endereco'],
                numero=request.POST['numero'],
                bairro=request.POST['bairro'],
                email=request.POST['email'],
                cidade_id=cidade_id
            )
            cliente.save()
            return redirect('clientes:lista')
        except Exception as e:
            return render(request, 'clientes/form.html', {'cidades': cidades, 'erro': str(e)})
    return render(request, 'clientes/form.html', {'cidades': cidades})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cidades = Cidade.objects.all()
    if request.method == 'POST':
        cliente.nome = request.POST['nome']
        cliente.cpf = request.POST['cpf']
        cliente.telefone = request.POST['telefone']
        cliente.endereco = request.POST['endereco']
        cliente.numero = request.POST['numero']
        cliente.bairro = request.POST['bairro']
        cliente.email = request.POST['email']
        cliente.cidade_id = request.POST['cidade']
        cliente.save()
        return redirect('clientes:lista')
    return render(request, 'clientes/form.html', {'cliente': cliente, 'cidades': cidades})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect('clientes:lista')
