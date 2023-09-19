from django.db import models


class Stand(models.Model):
    localizacao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.localizacao


class Reserva(models.Model):
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=20)
    nome_empresa = models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=50)
    quitado = models.BooleanField(default=False)

    def __str__(self):
        return self.stand
