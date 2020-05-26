from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from .forms import *
from .processa_csv import processa_arquivo_despesas_pagas_exercicio

def index(request):
    return render(request, 'menu.html', {})

def upload_file(request):
    if request.method == 'POST':
        form = DespesasPagasExercicioForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            json_file = processa_arquivo_despesas_pagas_exercicio(arquivo)
            return HttpResponse(json_file, content_type='application/json; charset=utf-8')
    else:
        form = DespesasPagasExercicioForm()
    return render(request, 'sigefes/upload.html', {'form': form})
