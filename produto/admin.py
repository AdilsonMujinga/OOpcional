from django.contrib import admin

from .models import Clientes, Produtos, Funcionarios

admin.site.register(Clientes)
admin.site.register(Produtos)
admin.site.register(Funcionarios)

