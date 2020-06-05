from django.forms import ModelForm

from reluci.models import PontoControle


class SintesePontoControleForm(ModelForm):

    class Meta:
        model = PontoControle
        fields = ['sintese']