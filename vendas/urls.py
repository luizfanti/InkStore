from django.urls import path
from . import views

app_name = 'vendas'

urlpatterns = [
    path('', views.lista_vendas, name='lista'),
    path('nova/', views.nova_venda, name='nova'),
    path('excluir/<int:id>/', views.excluir_venda, name='excluir'),
]
