from django import forms

class DespesasPagasExercicioForm(forms.Form):
    file = forms.FileField()