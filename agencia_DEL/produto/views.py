from django.shortcuts import render

def pagina_inicial(request):
    return render(request, 'produto/pagina_inicial.html')

def cadastrar_produto(request):
    return render(request, 'produto/cadastrar.html')

def visualizar_produto(request):
    return render(request, 'produto/visualizar.html')

def editar_produto(request, id):
    return render(request, 'produto/editar.html')

def remover_produto(request, id):
    return render(request, 'produto/remover.html')

def historico_produto(request):
    return render(request, 'produto/historico.html')
