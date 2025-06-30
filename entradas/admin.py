from django.contrib import admin
from .models import Entrada, ItemEntrada

class ItemEntradaInline(admin.TabularInline):
    model = ItemEntrada
    extra = 1

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fornecedor', 'dataEntrada')
    inlines = [ItemEntradaInline]

@admin.register(ItemEntrada)
class ItemEntradaAdmin(admin.ModelAdmin):
    list_display = ('entrada', 'produto', 'quantidade', 'preco')