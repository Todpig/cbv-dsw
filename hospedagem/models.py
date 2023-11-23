from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Quarto(models.Model):
    apartamento = models.IntegerField(null=True)
    valor = models.FloatField(null=True)

    def __str__(self):
        return str(self.apartamento)

class Hospedagem(models.Model):
    data_entrada = models.DateField(auto_now=True)
    data_saida = models.DateField(auto_now=False)
    valor = models.FloatField(null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente.nome
    
class Consumo(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField(auto_now=True)
    valor = models.FloatField(null=True)
    Hospedagem = models.ForeignKey(Hospedagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome