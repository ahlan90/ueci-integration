from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, CharField, TextInput, forms, HiddenInput, models

from reluci.models import PontoControle, AnalisePontoControle, ObservacaoTarefaAtividade


class AnalisePontoControleForm(ModelForm):

    class Meta:
        model = AnalisePontoControle
        fields = ['classificacao', 'status', 'analise', 'ponto_controle', 'user']
        widgets = {
            'ponto_controle': HiddenInput(),
            'user': HiddenInput()
        }


class AnalisePontoControleForm(ModelForm):

    class Meta:
        model = AnalisePontoControle
        fields = ['classificacao', 'status', 'analise', 'ponto_controle', 'user']
        widgets = {
            'ponto_controle': HiddenInput(),
            'user': HiddenInput()
        }


class ObservacaoTarefaForm(ModelForm):

    observacao = CharField(widget=CKEditorWidget(attrs={'id': 'id_observacao_tarefa'}))

    class Meta:
        model = ObservacaoTarefaAtividade
        fields = ['tarefa', 'status', 'observacao', 'user']
        widgets = {
            'user': HiddenInput(),
        }


class ObservacaoAtividadeForm(ModelForm):

    observacao = CharField(widget=CKEditorWidget(attrs={'id': 'id_observacao_atividade'}))

    class Meta:
        model = ObservacaoTarefaAtividade
        fields = ['atividade', 'status', 'observacao', 'user']
        widgets = {
            'user': HiddenInput()
        }
