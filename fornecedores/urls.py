from django.urls import path
from . import views

app_name = 'fornecedores'

urlpatterns = [
    path('', views.lista_fornecedores, name='lista'),
    path('novo/', views.novo_fornecedor, name='novo'),
    path('editar/<int:id>/', views.editar_fornecedor, name='editar'),
    path('excluir/<int:id>/', views.excluir_fornecedor, name='excluir'),
]
