import datetime
from datetime import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.template.loader import render_to_string
from django.views.generic import DetailView
from django_weasyprint import WeasyTemplateResponseMixin

from reluci.forms import AnalisePontoControleForm, ObservacaoForm
from reluci.models import ItemAbordagem, PontoControle, AnalisePontoControle, Tarefa, ObservacaoTarefaAtividade


class FolhaTrabalhoView(DetailView):
    model = PontoControle
    template_name = 'reluci/folha_trabalho_pdf.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ug'] = 'NOME DA UG DA SESP'
        context['codigo_ug'] = 'NOME DA UG DA SESP'
        context['exercicio'] = '2020'
        context['numero_folha_trabalho'] = '1'
        context['data_conclusao'] = datetime.now()

        return context


class FolhaTrabalhoPrintView(WeasyTemplateResponseMixin, FolhaTrabalhoView):
    # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        settings.STATIC_ROOT + '/apps/folha-trabalho.css',
    ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = True

    # suggested filename (is required for attachment!)
    pdf_filename = 'folha-trabalho.pdf'


def checklist_reluci(request):
    itens_abordagem = ItemAbordagem.objects.all()

    data = {
        'titulo': 'Reluci',
        'itens_abordagem': itens_abordagem,
        'menu': 'active',
        'sidebar': 'active'
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
def save_analise_ponto_controle_form(request, form, pk, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            ponto_controle = get_object_or_404(PontoControle, pk=pk)
            data['html_analise_ponto_controle_list'] = render_to_string(
                'reluci/ponto-controle/lista_analise_ponto_controle_parcial.html', {
                    'ponto_controle': ponto_controle
                })
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

    if request.method == 'POST':
        form = AnalisePontoControleForm(request.POST or None)
    else:
        form = AnalisePontoControleForm(initial={'ponto_controle': ponto_controle, 'user': request.user})

    return save_analise_ponto_controle_form(request, form, pk, 'reluci/ponto-controle/cria_ponto_controle_modal.html')


@login_required
def analise_ponto_controle_update(request, pk):
    analise_ponto_controle = get_object_or_404(AnalisePontoControle, pk=pk)
    if request.method == 'POST':
        form = AnalisePontoControleForm(request.POST, instance=analise_ponto_controle)
    else:
        form = AnalisePontoControleForm(instance=analise_ponto_controle)
    return save_analise_ponto_controle_form(request, form, pk,
                                            'reluci/ponto-controle/atualiza_ponto_controle_modal.html')


@login_required
def save_observacao_tarefa_form(request, form, pk, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    context = {
        'form': form,
        'observacao_id': pk,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def observacao_tarefa_create(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        form = ObservacaoForm(request.POST or None)
    else:
        form = ObservacaoForm(initial={'tarefa': tarefa, 'user': request.user})

    return save_observacao_tarefa_form(request, form, pk, 'reluci/tarefa/cria_observacao_tarefa_modal.html')


@login_required
def observacao_tarefa_update(request, pk):
    observacao_tarefa = get_object_or_404(ObservacaoTarefa, pk=pk)

    if request.method == 'POST':
        form = ObservacaoForm(request.POST, instance=observacao_tarefa)
    else:
        form = ObservacaoForm(instance=observacao_tarefa)
    return save_observacao_tarefa_form(request, form, pk, 'reluci/tarefa/atualiza_observacao_tarefa_modal.html')


@login_required
def ponto_controle_detail(request, pk):

    itens_abordagem = ItemAbordagem.objects.all()

    ponto_controle = get_object_or_404(PontoControle, pk=pk)

    if request.method == 'POST':
        form_analise = AnalisePontoControleForm(request.POST)
        form_observacao = ObservacaoForm(request.POST)

        if form_observacao.is_valid():
            form_observacao.save()
            return redirect('ponto_controle_detail', pk)

        if form_analise.is_valid():
            form_analise.save()
            return redirect('ponto_controle_detail', pk)
    else:
        form_analise = AnalisePontoControleForm(
            initial={'ponto_controle': ponto_controle, 'user': request.user})
        form_observacao = ObservacaoForm(initial={'user': request.user}, ponto_controle=ponto_controle)

    data = {
        'titulo': 'Ponto de Controle ' + ponto_controle.get_codigo_completo(),
        'itens_abordagem': itens_abordagem,
        'ponto_controle': ponto_controle,
        'form_analise': form_analise,
        'form_observacao': form_observacao,
        'sidebar': 'active'
    }

    return render(request, 'reluci/ponto-controle/ponto_controle_detail.html', data)


@login_required
def ponto_controle_detail_analise(request, pk):

    itens_abordagem = ItemAbordagem.objects.all()

    analise = get_object_or_404(AnalisePontoControle, pk=pk)

    ponto_controle = get_object_or_404(PontoControle, pk=analise.ponto_controle.id)

    form_analise = AnalisePontoControleForm(instance=analise)

    form_observacao = ObservacaoForm(initial={'user': request.user}, ponto_controle=ponto_controle)

    data = {
        'titulo': 'Ponto de Controle ' + ponto_controle.get_codigo_completo(),
        'itens_abordagem': itens_abordagem,
        'ponto_controle': ponto_controle,
        'form_analise': form_analise,
        'form_observacao': form_observacao,
        'sidebar': 'active'
    }

    return render(request, 'reluci/ponto-controle/ponto_controle_detail.html', data)


@login_required
def ponto_controle_detail_observacao(request, pk):

    itens_abordagem = ItemAbordagem.objects.all()

    observacao = get_object_or_404(ObservacaoTarefaAtividade, pk=pk)

    ponto_controle = get_object_or_404(PontoControle, pk=observacao.ponto_controle.id)

    form_analise = AnalisePontoControleForm(
        initial={'ponto_controle': ponto_controle, 'user': request.user})

    form_observacao = ObservacaoForm(instance=observacao)

    data = {
        'titulo': 'Ponto de Controle ' + ponto_controle.get_codigo_completo(),
        'itens_abordagem': itens_abordagem,
        'ponto_controle': ponto_controle,
        'form_analise': form_analise,
        'form_observacao': form_observacao,
        'sidebar': 'active'
    }

    return render(request, 'reluci/ponto-controle/ponto_controle_detail.html', data)