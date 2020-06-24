from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, CharField, TextInput, forms, HiddenInput, models

from reluci.models import PontoControle, AnalisePontoControle, ObservacaoTarefaAtividade, Tarefa, Atividade


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


class ObservacaoForm(ModelForm):

    observacao = CharField(widget=CKEditorWidget(attrs={'id': 'id_observacao_tarefa'}))

    class Meta:
        model = ObservacaoTarefaAtividade
        fields = ['tarefa', 'atividade', 'status', 'observacao', 'user']
        widgets = {
            'user': HiddenInput(),
        }

    def __init__(self, *args, ponto_controle=None, **kwargs):
        super(ObservacaoForm, self).__init__(*args, **kwargs)
        if ponto_controle:
            tarefas = Tarefa.objects.filter(ponto_controle=ponto_controle)
            self.fields['tarefa'].queryset = tarefas
            self.fields['atividade'].queryset = Atividade.objects.filter(tarefa__in=tarefas)



# class ObservacaoAtividadeForm(ModelForm):
#
#     observacao = CharField(widget=CKEditorWidget(attrs={'id': 'id_observacao_atividade'}))
#
#     class Meta:
#         model = ObservacaoTarefaAtividade
#         fields = ['atividade', 'status', 'observacao', 'user']
#         widgets = {
#             'user': HiddenInput()
#         }
