"""
URL configuration for projecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))



    from django.contrib import admin
from django.urls import path
from produto import views

urlpatterns = [
    path('pagina_inicial', views.pagina_inicial, name='pagina_inicial'),
   
]
# path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
  #  path('visualizar/', views.visualizar_produto, name='visualizar_produto'),
   # path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
   ## path('historico/', views.historico_produto, name='historico_produto'),


   
#def editar_produto(request, id):
    return render(request, 'produto/editar.html')

#def remover_produto(request, id):
    return render(request, 'produto/remover.html')


    from django.shortcuts import render

def pagina(request):
    return render(request, 'produto/pagina.html')

def clientes(request):
    return render(request, 'produto/clientes.html')

def produtos(request):
    return render(request, 'produto/produtos.html')

def funcionarios(request):
    return render(request, 'produto/funcionarios.html')

"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produto.urls')),  # Aqui vou incluir todas as rotas da tua app produto
]
