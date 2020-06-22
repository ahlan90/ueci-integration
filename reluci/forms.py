from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, CharField, TextInput, forms, HiddenInput

from reluci.models import PontoControle, AnalisePontoControle, ObservacaoTarefa, ObservacaoAtividade


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

    class Meta:
        model = ObservacaoTarefa
        fields = ['status', 'observacao', 'tarefa', 'user']
        widgets = {
            'tarefa': HiddenInput(),
            'user': HiddenInput()
        }


class ObservacaoAtividadeForm(ModelForm):

    class Meta:
        model = ObservacaoAtividade
        fields = ['status', 'observacao', 'atividade', 'user']
        widgets = {
            'atividade': HiddenInput(),
            'user': HiddenInput()
        }
