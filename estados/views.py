from django.shortcuts import render, redirect, get_object_or_404
from .models import Estado

def lista_estados(request):
    estados = Estado.objects.all()
    return render(request, 'estados/lista.html', {'estados': estados})

def novo_estado(request):
    if request.method == 'POST':
        Estado.objects.create(
            nome=request.POST['nome'],
            sigla=request.POST['sigla'],
        )
        return redirect('estados:lista')
    return render(request, 'estados/form.html')

def editar_estado(request, id):
    estado = get_object_or_404(Estado, pk=id)
    if request.method == 'POST':
        estado.nome = request.POST['nome']
        estado.sigla = request.POST['sigla']
        estado.save()
        return redirect('estados:lista')
    return render(request, 'estados/form.html', {'estado': estado})

def excluir_estado(request, id):
    estado = get_object_or_404(Estado, pk=id)
    estado.delete()
    return redirect('estados:lista')
