from django.urls import path
from . import views

app_name = 'entradas'

urlpatterns = [
    path('', views.lista_entradas, name='lista'),
    path('nova/', views.nova_entrada, name='nova'),
    path('excluir/<int:id>/', views.excluir_entrada, name='excluir'),
]
