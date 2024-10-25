from django.db import models

# Create your models here.
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Comanda(models.Model):
    codigo_comanda = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=[('Aberta', 'Aberta'), ('Finalizada', 'Finalizada')])
    quantidade = models.PositiveBigIntegerField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.codigo_comanda
    
class ItemComanda(models.Model):  # Certifique-se de que o nome está correto aqui
    comanda = models.ForeignKey(Comanda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    papel = models.CharField(max_length=20, choices=[('Atendente', 'Atendente'), ('Caixa', 'Caixa')])

    def __str__(self): 
        return self.nome
