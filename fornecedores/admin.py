from django.contrib import admin
from .models import Fornecedor

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj', 'telefone', 'email')
    search_fields = ('nome', 'cnpj')