from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, CharField, TextInput

from reluci.models import PontoControle


class PontoControleForm(ModelForm):

    class Meta:
        model = PontoControle
        fields = ['analise']