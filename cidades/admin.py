from django.contrib import admin
from .models import Cidade

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'estado')
    search_fields = ('nome',)