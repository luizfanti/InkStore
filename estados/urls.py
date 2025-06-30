from django.urls import path
from . import views

app_name = 'estados'

urlpatterns = [
    path('', views.lista_estados, name='lista'),
    path('novo/', views.novo_estado, name='novo'),
    path('editar/<int:id>/', views.editar_estado, name='editar'),
    path('excluir/<int:id>/', views.excluir_estado, name='excluir'),
]
