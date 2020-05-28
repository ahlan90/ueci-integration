from django.db import models

# Create your models here.
class UnidadeGestora(models.Model):

    codigo = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo


class Credor(models.Model):

    cpf_cnpj = models.CharField(max_length=20)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.cpf_cnpj + ' - ' + self.nome


class Processo(models.Model):

    numero = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.numero


class NotaLiquidacao(models.Model):

    numero = models.CharField(max_length=50)
    data = models.DateField(null=True)

    historico = models.TextField()

    def __str__(self):
        return self.numero


class NotaEmpenho(models.Model):

    numero = models.CharField(max_length=50)
    data = models.DateField(null=True)

    historico = models.TextField()

    def __str__(self):
        return self.numero


class Despesa(models.Model):

    unidade_gestora = models.ForeignKey(UnidadeGestora, on_delete=models.CASCADE)
    credor = models.ForeignKey(Credor, on_delete=models.CASCADE)
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)


class DespesaLiquidada(Despesa):

    valor_liquidado = models.DecimalField(max_digits=20, decimal_places=2)
    nota_liquidacao = models.ForeignKey(NotaLiquidacao, on_delete=models.CASCADE)


class DespesaEmpenhada(Despesa):

    valor_empenhado = models.DecimalField(max_digits=20, decimal_places=2)
    nota_empenho = models.ForeignKey(NotaEmpenho, on_delete=models.CASCADE)
