from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Sin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import DetailView
from django_weasyprint import WeasyTemplateResponseMixin

from reluci.forms import AnalisePontoControleForm
from reluci.models import ItemAbordagem, PontoControle, AnalisePontoControle


class FolhaTrabalhoView(DetailView):

    model = PontoControle
    template_name = 'reluci/folha_trabalho_pdf.html'


class FolhaTrabalhoPrintView(WeasyTemplateResponseMixin, FolhaTrabalhoView):

    # output of MyModelView rendered as PDF with hardcoded CSS
    pdf_stylesheets = [
        settings.STATIC_ROOT + '/apps/folha-trabalho.css',
    ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False

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
    return save_analise_ponto_controle_form(request, form, pk, 'reluci/ponto-controle/atualiza_ponto_controle_modal.html')


@login_required
def ponto_controle_detail(request, pk):

    itens_abordagem = ItemAbordagem.objects.all()

    ponto_controle = get_object_or_404(PontoControle, pk=pk)

    form = AnalisePontoControleForm(initial={'ponto_controle': ponto_controle, 'user': request.user})

    data = {
        'titulo': 'Ponto de Controle ' + ponto_controle.get_codigo_completo(),
        'itens_abordagem': itens_abordagem,
        'ponto_controle': ponto_controle,
        'form': form,
        'sidebar': 'active'
    }

    return render(request, 'reluci/ponto-controle/ponto_controle_detail.html', data)

