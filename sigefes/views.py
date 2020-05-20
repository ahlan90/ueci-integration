from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from .processa_csv import processa_arquivo_despesas_pagas_exercicio


def upload_file(request):
    if request.method == 'POST':
        form = DespesasPagasExercicioForm(request.POST, request.FILES)
        if form.is_valid():
            processa_arquivo_despesas_pagas_exercicio(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = DespesasPagasExercicioForm()
    return render(request, 'sigefes/upload.html', {'form': form})
