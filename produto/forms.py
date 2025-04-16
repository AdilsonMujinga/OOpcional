from django import forms
from .models import Clientes, Produtos, Funcionarios

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = '__all__'

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = '__all__'
