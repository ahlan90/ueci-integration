from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, CharField, TextInput, forms, HiddenInput

from reluci.models import PontoControle, AnalisePontoControle


class AnalisePontoControleForm(ModelForm):

    class Meta:
        model = AnalisePontoControle
        fields = ['classificacao', 'status', 'analise', 'ponto_controle', 'user']
        widgets = {
            'ponto_controle': HiddenInput(),
            'user': HiddenInput()
        }
