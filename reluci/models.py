from ckeditor.fields import RichTextField
from django.db import models


class ItemAbordagem(models.Model):

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.codigo + " - " + self.nome


class ItemGestao(models.Model):

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300, null=True, blank=True)

    item = models.ForeignKey(ItemAbordagem, on_delete=models.CASCADE, null=True, blank=True, related_name='itens_gestao')

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

    ponto_controle_relacionado = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    grupo = models.ForeignKey(ItemGestao, on_delete=models.CASCADE, related_name='pontos')

    CLASSIFICACOES = (
        ('ATENDE', 'Atende'),
        ('ATENDE_PARCIALMENTE', 'Atende parcialmente'),
        ('NAO_ATENDE', 'Não atende'),
    )

    classificacao = models.CharField(max_length=30, choices=CLASSIFICACOES, null=True, blank=True)

    STATUS = (
        ('NAO_INICIADO', 'Não iniciado'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('AGUARDANDO', 'Aguardando'),
        ('FINALIZADO', 'Finalizado'),
    )
    status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')
    analise = RichTextField()

    def __str__(self):
        return self.get_codigo_completo() + " - " + self.nome

    def get_codigo_completo(self):
        if self.grupo:
            return self.grupo.get_codigo_completo() + '.' + self.codigo
        else:
            return self.codigo


class SubPontoControle(models.Model):

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=1000, null=True, blank=True)

    ponto_controle = models.ForeignKey(
        PontoControle,
        on_delete=models.CASCADE,
        null=True,
        blank=True, related_name='sub_pontos_controle')

    STATUS = (
        ('NAO_INICIADO', 'Não iniciado'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('AGUARDANDO', 'Aguardando'),
        ('FINALIZADO', 'Finalizado'),
    )
    status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')

    CLASSIFICACOES = (
        ('ATENDE', 'Atende'),
        ('ATENDE_PARCIALMENTE', 'Atende parcialmente'),
        ('NAO_ATENDE', 'Não atende'),
    )
    classificacao = models.CharField(max_length=30, choices=CLASSIFICACOES, null=True, blank=True)

    observacao = RichTextField()

    def __str__(self):
        return self.get_codigo_completo() + " - " + self.nome

    def get_codigo_completo(self):
        if self.ponto_controle:
            return self.ponto_controle.get_codigo_completo() + '.' + self.codigo
        else:
            return self.codigo


class Tarefa(models.Model):

    codigo = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)
    observacao = RichTextField()

    STATUS = (
        ('NAO_INICIADO', 'Não iniciado'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('AGUARDANDO', 'Aguardando'),
        ('FINALIZADO', 'Finalizado'),
    )
    status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')

    ponto_controle = models.ForeignKey(
        PontoControle,
        on_delete=models.CASCADE,
        related_name='tarefas', null=True, blank=True)

    sub_ponto_controle = models.ForeignKey(
        SubPontoControle,
        on_delete=models.CASCADE,
        related_name='tarefas', null=True, blank=True)

    def get_codigo_completo(self):
        if self.ponto_controle:
            return self.ponto_controle.get_codigo_completo() + '.' + self.codigo
        else:
            if self.sub_ponto_controle:
                return self.sub_ponto_controle.get_codigo_completo() + '.' + self.codigo
            return self.codigo


class Atividade(models.Model):

    descricao = models.TextField(null=True, blank=True)
    observacao = RichTextField()

    STATUS = (
        ('NAO_INICIADO', 'Não iniciado'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('AGUARDANDO', 'Aguardando'),
        ('FINALIZADO', 'Finalizado'),
    )
    status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')

    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='atividades', null=True)

    def __str__(self):
        return self.descricao