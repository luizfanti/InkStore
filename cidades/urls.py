from django.urls import path
from . import views

app_name = 'cidades'

urlpatterns = [
    path('', views.lista_cidades, name='lista'),
    path('nova/', views.nova_cidade, name='nova'),
    path('editar/<int:id>/', views.editar_cidade, name='editar'),
    path('excluir/<int:id>/', views.excluir_cidade, name='excluir'),
]
