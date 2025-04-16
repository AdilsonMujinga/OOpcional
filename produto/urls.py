
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina, name='pagina'),  # Página inicial
    path('clientes/', views.clientes, name='clientes'),  # Página de cadastro
    path('produtos/', views.produtos, name='produtos'),
    path('funcionarios/', views.funcionarios, name='funcionarios'),
]
