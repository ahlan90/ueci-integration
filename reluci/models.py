from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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

    item = models.ForeignKey(ItemAbordagem,
                             on_delete=models.CASCADE, null=True,
                             blank=True, related_name='itens_gestao')

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=300, null=True, blank=True)
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

    ponto_controle_relacionado = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    grupo = models.ForeignKey(ItemGestao, on_delete=models.CASCADE, related_name='pontos')

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=1000, null=True, blank=True)

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
    data_criacao = models.DateTimeField(default=timezone.now, null=True, blank=True)


    def __str__(self):
        return 'Ponto de Controle: ' + self.ponto_controle.get_codigo_completo() + ' - Usuário: ' + str(self.user)

    class Meta:
        ordering = ('-criado',)


class SubPontoControle(models.Model):

    ponto_controle = models.ForeignKey(
        PontoControle,
        on_delete=models.CASCADE,
        null=True,
        blank=True, related_name='sub_pontos_controle')

    codigo = models.CharField(max_length=50)
    nome = models.CharField(max_length=300)
    descricao = models.CharField(max_length=1000, null=True, blank=True)

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
    status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')
    classificacao = models.CharField(max_length=30, choices=CLASSIFICACOES, default='NAO_AVALIADO')


class Tarefa(models.Model):

    ponto_controle = models.ForeignKey(
        PontoControle,
        on_delete=models.CASCADE,
        related_name='tarefas', null=True, blank=True)

    sub_ponto_controle = models.ForeignKey(
        SubPontoControle,
        on_delete=models.CASCADE,
        related_name='tarefas', null=True, blank=True)

    codigo = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)

    def get_codigo_completo(self):
        if self.ponto_controle:
            return self.ponto_controle.get_codigo_completo() + '.' + self.codigo
        else:
            if self.sub_ponto_controle:
                return self.sub_ponto_controle.get_codigo_completo() + '.' + self.codigo
            return self.codigo

    def get_status_detail(self):
        observacao = self.observacoes_tarefa.last()
        if observacao:
            return observacao.status
        else:
            return STATUS[0][0]

    def __str__(self):
        return self.get_codigo_completo()

    class Meta:
        ordering = ('codigo',)


class Atividade(models.Model):

    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name='atividades', null=True)

    codigo = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    #status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')

    def get_codigo_completo(self):
        if self.tarefa:
            return self.tarefa.get_codigo_completo() + '.' + str(self.codigo)

        return self.codigo

    def __str__(self):
        return self.get_codigo_completo()

    class Meta:
        ordering = ('codigo',)


class ObservacaoTarefaAtividade(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE,
                               null=True, related_name='observacoes_tarefa')
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, blank=True,
                                  null=True, related_name='observacoes_atividade')

    status = models.CharField(max_length=30, choices=STATUS, default='NAO_INICIADO')
    data_criacao = models.DateTimeField(default=timezone.now, null=True, blank=True)
    observacao = RichTextField()

    def __str__(self):
        return self.observacao