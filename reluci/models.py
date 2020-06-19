from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

STATUS = (
    ('NAO_INICIADO', 'Não iniciado'),
    ('EM_ANDAMENTO', 'Em andamento'),
    ('AGUARDANDO', 'Aguardando'),
    ('FINALIZADO', 'Finalizado'),
)

CLASSIFICACOES = (
    ('NAO_AVALIADO', 'Não avaliado'),
    ('ATENDE', 'Atende'),
    ('ATENDE_PARCIALMENTE', 'Atende parcialmente'),
    ('NAO_ATENDE', 'Não atende'),
)

class ItemAbordagem(models.Model):

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.codigo + " - " + self.nome

    class Meta:
        ordering = ('codigo',)


class ItemGestao(models.Model):

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300, null=True, blank=True)

    item = models.ForeignKey(ItemAbordagem,
                             on_delete=models.CASCADE, null=True,
                             blank=True, related_name='itens_gestao')

    percentual = models.IntegerField(default=0)

    def __str__(self):
        return self.get_codigo_completo() + " - " + self.nome

    def get_codigo_completo(self):
        if self.item:
            return self.item.codigo + "." + self.codigo
        else:
            return self.codigo

    class Meta:
        ordering = ('codigo',)


class PontoControle(models.Model):

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=1000, null=True, blank=True)

    ponto_controle_relacionado = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    grupo = models.ForeignKey(ItemGestao, on_delete=models.CASCADE, related_name='pontos')

    def __str__(self):
        return self.get_codigo_completo() + " - " + self.nome

    def get_codigo_completo(self):
        if self.grupo:
            return self.grupo.get_codigo_completo() + '.' + self.codigo
        else:
            return self.codigo

    def get_status_detail(self):
        analise: AnalisePontoControle = self.analises.last()
        if analise:
            return analise.status
        else:
            return STATUS

    class Meta:
        ordering = ('codigo',)


class AnalisePontoControle(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ponto_controle = models.ForeignKey(PontoControle, on_delete=models.CASCADE, related_name='analises')
    analise = RichTextField("Análise", null=True, blank=True)

    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')
    classificacao = models.CharField("Classificação", max_length=30, choices=CLASSIFICACOES, default='NAO_AVALIADO')

    def __str__(self):
        return 'Ponto de Controle: ' + self.ponto_controle.get_codigo_completo() + ' - Usuário: ' + str(self.user)

    class Meta:
        ordering = ('-criado',)

class SubPontoControle(models.Model):

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=1000, null=True, blank=True)

    ponto_controle = models.ForeignKey(
        PontoControle,
        on_delete=models.CASCADE,
        null=True,
        blank=True, related_name='sub_pontos_controle')


    def __str__(self):
        return self.get_codigo_completo() + " - " + self.nome

    def get_codigo_completo(self):
        if self.ponto_controle:
            return self.ponto_controle.get_codigo_completo() + '.' + self.codigo
        else:
            return self.codigo

    class Meta:
        ordering = ('codigo',)


class AnaliseSubPontoControle(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_ponto_controle = models.ForeignKey(SubPontoControle, on_delete=models.CASCADE)
    analise = RichTextField(null=True, blank=True)

    STATUS = (
        ('NAO_INICIADO', 'Não iniciado'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('AGUARDANDO', 'Aguardando'),
        ('FINALIZADO', 'Finalizado'),
    )
    status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')

    classificacao = models.CharField(max_length=30, choices=CLASSIFICACOES, default='NAO_AVALIADO')


class Tarefa(models.Model):

    codigo = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)

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

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ('codigo',)


class ObservacaoTarefa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
    observacao = RichTextField()


class Atividade(models.Model):

    codigo = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

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

    class Meta:
        ordering = ('codigo',)


class ObservacaoAtividade(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    observacao = RichTextField()
