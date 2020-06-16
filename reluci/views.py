from django.contrib.auth.decorators import login_required
from django.db.models.functions import Sin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string

from reluci.forms import AnalisePontoControleForm
from reluci.models import ItemAbordagem, PontoControle, AnalisePontoControle


def checklist_reluci(request):

    itens_abordagem = ItemAbordagem.objects.all()

    data = {
        'titulo': 'Reluci',
        'itens_abordagem': itens_abordagem
    }

    return render(request, 'reluci/checklist.html', data)


@login_required
def relato_ponto_controle(request, pk):

    ponto = get_object_or_404(PontoControle, pk=pk)

    data = {
        'ponto': ponto
    }

    return render(request, 'reluci/atividades.html', data)


@login_required
def save_ponto_controle_form(request, form, pk, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    context = {
        'form': form,
        'ponto_controle_id': pk,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def analise_ponto_controle_create(request, pk):

    ponto_controle = get_object_or_404(PontoControle, pk=pk)
    data = {
        'ponto_controle_id': pk
    }
    if request.method == 'POST':
        form = AnalisePontoControleForm(request.POST or None)
    else:
        form = AnalisePontoControleForm(initial={'ponto_controle': ponto_controle, 'user': request.user})

    return save_ponto_controle_form(request, form, pk, 'reluci/ponto-controle/cria_ponto_controle_modal.html')


@login_required
def analise_ponto_controle_update(request, pk):
    ponto_controle = get_object_or_404(PontoControle, pk=pk)
    analise = AnalisePontoControle.objects.filter(ponto_controle=ponto_controle).order_by('criado')[0]
    if request.method == 'POST':
        form = AnalisePontoControleForm(request.POST, instance=analise)
    else:
        form = AnalisePontoControleForm(instance=analise)
    return save_ponto_controle_form(request, form, pk, 'reluci/ponto-controle/atualiza_ponto_controle_modal.html')


@login_required
def ponto_controle_detail(request, pk):

    itens_abordagem = ItemAbordagem.objects.all()

    ponto_controle = get_object_or_404(PontoControle, pk=pk)

    form = AnalisePontoControleForm(initial={'ponto_controle': ponto_controle, 'user': request.user})

    data = {
        'titulo': 'Ponto de Controle ' + ponto_controle.get_codigo_completo(),
        'menu': 'active',
        'itens_abordagem': itens_abordagem,
        'ponto_controle': ponto_controle,
        'form': form
    }

    return render(request, 'reluci/ponto-controle/ponto_controle_detail.html', data)

