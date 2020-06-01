from django import forms

class DespesasLiquidadasExcelForm(forms.Form):
    arquivo = forms.FileField()

class DespesasEmpenhadasExercicioForm(forms.Form):
    arquivo = forms.FileField()
