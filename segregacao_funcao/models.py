from django.db import models

# Create your models here.
from sigefes.models import UnidadeGestora

class ContaContribuicao(models.Model):

    codigo = models.CharField(max_length=50, null=True)
    descricao = models.CharField(max_length=250, null=True)


class DespesaPrevidenciariaPatronal(models.Model):

    unidade_gestora = models.ForeignKey(UnidadeGestora, on_delete=models.CASCADE)
    conta = models.ForeignKey(ContaContribuicao, on_delete=models.CASCADE)
    mes = models.IntegerField()
    saldo = models.DecimalField(max_digits=15, decimal_places=2)
