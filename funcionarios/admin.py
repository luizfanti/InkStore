from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'telefone', 'email')
    search_fields = ('nome', 'cpf', 'email')