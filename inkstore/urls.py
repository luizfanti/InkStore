from django.contrib import admin
from django.urls import path, include
from inkstore.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
]
