from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    data_contratacao = models.DateField()

    def __str__(self):
        return self.nome

