from django.shortcuts import render, get_object_or_404

# Create your views here.
from reluci.forms import SintesePontoControleForm
from reluci.models import ItemAbordagem, PontoControle


def checklist_reluci(request):

    itens = ItemAbordagem.objects.all().order_by('codigo')

    form = SintesePontoControleForm()

    data = {
        'itens': itens,
        'form': form
    }

    return render(request, 'reluci/checklist.html', data)

def relato_ponto_controle(request, pk):

    ponto = get_object_or_404(PontoControle, pk=pk)

    data = {
        'ponto': ponto
    }

    return render(request, 'reluci/relato_ponto_controle.html', data)
