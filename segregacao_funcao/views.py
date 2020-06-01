from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from segregacao_funcao.forms import ContribuicaoPatronalForm
from segregacao_funcao.processa_dados import processa_arquivo_contribuicao_patronal


def contribuicao_patronal_upload(request):

    if request.method == 'POST':
        form = ContribuicaoPatronalForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            json_file = processa_arquivo_contribuicao_patronal(arquivo)
            return HttpResponse(json_file, content_type='application/json; charset=utf-8')
    else:
        form = ContribuicaoPatronalForm()
    return render(request, 'segregacao_funcao/contribuicao_patronal_upload.html', {'form': form})

