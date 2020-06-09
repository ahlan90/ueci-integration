from django.db.models.functions import Sin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string

from reluci.forms import PontoControleForm
from reluci.models import ItemAbordagem, PontoControle


def checklist_reluci(request):

    itens_abordagem = ItemAbordagem.objects.all().order_by('codigo')

    data = {
        'itens_abordagem': itens_abordagem
    }

    return render(request, 'reluci/checklist.html', data)


def relato_ponto_controle(request, pk):

    ponto = get_object_or_404(PontoControle, pk=pk)

    data = {
        'ponto': ponto
    }

    return render(request, 'reluci/atividades.html', data)


def save_ponto_controle_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def ponto_controle_create(request):
    if request.method == 'POST':
        form = PontoControleForm(request.POST)
    else:
        form = PontoControleForm()
    return save_ponto_controle_form(request, form, 'reluci/ponto-controle/cria_ponto_controle_modal.html')


def ponto_controle_update(request, pk):
    ponto_controle = get_object_or_404(PontoControle, pk=pk)
    if request.method == 'POST':
        form = PontoControleForm(request.POST, instance=ponto_controle)
    else:
        form = PontoControleForm(instance=ponto_controle)
    return save_ponto_controle_form(request, form, 'reluci/ponto-controle/atualiza_ponto_controle_modal.html')

