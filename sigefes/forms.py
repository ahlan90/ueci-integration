from django import forms

class DespesasPagasExercicioForm(forms.Form):
    arquivo = forms.FileField()
