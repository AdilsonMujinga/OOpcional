from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco= models.EmailField()
    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    origem = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    tipo_produto = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=30)
    

    def __str__(self):
        return self.nome

