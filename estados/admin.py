from django.contrib import admin
from .models import Estado

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sigla')
    search_fields = ('nome', 'sigla')