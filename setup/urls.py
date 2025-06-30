from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inkstore.urls')),
    path('clientes/', include('clientes.urls')),
    path('produtos/', include('produtos.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('vendas/', include('vendas.urls')),
    path('entradas/', include('entradas.urls')),
    path('estados/', include('estados.urls')),
    path('cidades/', include('cidades.urls')),

]
