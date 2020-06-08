from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, CharField, TextInput

from reluci.models import PontoControle


class SintesePontoControleForm(ModelForm):

    class Meta:
        model = PontoControle
        fields = ['analise']

    def __init__(self, *args, **kwargs):
        super(SintesePontoControleForm, self).__init__(*args, **kwargs)
        self.fields['analise'].widget.attrs['id'] = 'teste' + self.instance.codigo
