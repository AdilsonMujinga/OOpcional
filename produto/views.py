from django.shortcuts import render, redirect
from .forms import ClienteForm, ProdutoForm, FuncionarioForm

def pagina(request):
    return render(request, 'produto/pagina.html')

def clientes(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    return render(request, 'produto/clientes.html', {'form': form})

def produtos(request):
    form = ProdutoForm()
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    return render(request, 'produto/produtos.html', {'form': form})

def funcionarios(request):
    form = FuncionarioForm()
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios')
    return render(request, 'produto/funcionarios.html', {'form': form})

def motorista(request):
    return render(request, 'produto/motorista.html')

def transporte(request):
    return render(request, 'produto/transporte.html')
