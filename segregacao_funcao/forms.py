from django import forms


class ContribuicaoPatronalForm(forms.Form):
    arquivo = forms.FileField()
