from django.shortcuts import render, redirect, get_object_or_404
from .models import Cidade
from estados.models import Estado

def lista_cidades(request):
    cidades = Cidade.objects.all()
    return render(request, 'cidades/lista.html', {'cidades': cidades})

def nova_cidade(request):
    estados = Estado.objects.all()
    if request.method == 'POST':
        Cidade.objects.create(
            nome=request.POST['nome'],
            estado_id=request.POST['estado'],
        )
        return redirect('cidades:lista')
    return render(request, 'cidades/form.html', {'estados': estados})

def editar_cidade(request, id):
    cidade = get_object_or_404(Cidade, pk=id)
    estados = Estado.objects.all()
    if request.method == 'POST':
        cidade.nome = request.POST['nome']
        cidade.estado_id = request.POST['estado']
        cidade.save()
        return redirect('cidades:lista')
    return render(request, 'cidades/form.html', {'cidade': cidade, 'estados': estados})

def excluir_cidade(request, id):
    cidade = get_object_or_404(Cidade, pk=id)
    cidade.delete()
    return redirect('cidades:lista')
