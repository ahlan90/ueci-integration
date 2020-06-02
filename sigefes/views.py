from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from .forms import *
from .processa_dados import processa_arquivo_despesas_liquidadas_exercicio

def index(request):
    return render(request, 'menu.html', {})

def despesa_liquidada_upload(request):

    if request.method == 'POST':
        form = DespesasLiquidadasExcelForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            json_file = processa_arquivo_despesas_liquidadas_exercicio(arquivo)
            return HttpResponse(json_file, content_type='application/json; charset=utf-8')
    else:
        form = DespesasLiquidadasExcelForm()
    return render(request, 'sigefes/contribuicao_patronal_upload.html', {'form': form})
