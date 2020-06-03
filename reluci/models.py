from django.db import models

class ItensPontoControle(models.Model):

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.codigo + " - " + self.nome


class GrupoPontoControle(models.Model):

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300, null=True, blank=True)

    item = models.ForeignKey(ItensPontoControle, on_delete=models.CASCADE, null=True, blank=True, related_name='grupos')

    ponto_controle_relacionado = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.get_codigo_completo() + " - " + self.nome

    def get_codigo_completo(self):
        if self.item:
            return self.item.codigo + "." + self.codigo
        else:
            return self.codigo


class PontoControle(models.Model):

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=1000, null=True, blank=True)

    grupo = models.ForeignKey(GrupoPontoControle, on_delete=models.CASCADE, related_name='pontos')

    CLASSIFICACOES = (
        ('ATENDE', 'Atende'),
        ('ATENDE_PARCIALMENTE', 'Atende parcialmente'),
        ('NAO_ATENDE', 'Não atende'),
    )

    classificacao = models.CharField(max_length=30, choices=CLASSIFICACOES, null=True, blank=True)

    STATUS = (
        ('NAO_INICIADO', 'Não iniciado'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('FINALIZADO', 'Finalizado'),
    )

    status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')

    def __str__(self):
        return self.get_codigo_completo() + " - " + self.nome

    def get_codigo_completo(self):
        if self.grupo:
            return self.grupo.get_codigo_completo() + '.' + self.codigo
        else:
            return self.codigo


class Atividade(models.Model):

    codigo = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)

    STATUS = (
        ('NAO_INICIADO', 'Não iniciado'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('FINALIZADO', 'Finalizado'),
    )

    status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')

    ponto_controle = models.ForeignKey(PontoControle, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo + " - " + self.descricao