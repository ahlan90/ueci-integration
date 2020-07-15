from django.db import models


class Entidade(models.Model):

    nome = models.CharField(max_length=300)
    sigla = models.CharField(max_length=30)
    entidade_auditora = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome