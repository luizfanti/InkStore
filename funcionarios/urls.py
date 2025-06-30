from django.urls import path
from . import views

app_name = 'funcionarios'

urlpatterns = [
    path('', views.lista_funcionarios, name='lista'),
    path('novo/', views.novo_funcionario, name='novo'),
    path('editar/<int:id>/', views.editar_funcionario, name='editar'),
    path('excluir/<int:id>/', views.excluir_funcionario, name='excluir'),
]
