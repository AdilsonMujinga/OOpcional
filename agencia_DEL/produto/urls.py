from django.urls import path
from . import views

urlpatterns = [
    path('pagina_inicial/', views.pagina_inicial, name='pagina_inicial'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('visualizar/', views.visualizar_produto, name='visualizar_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('remover/<int:id>/', views.remover_produto, name='remover_produto'),
    path('historico/', views.historico_produto, name='historico_produto'),
]
