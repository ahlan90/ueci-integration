from django.shortcuts import render

# Create your views here.
from reluci.models import ItemAbordagem


def checklist_reluci(request):

    itens = ItemAbordagem.objects.all().order_by('codigo')

    data = {
        'itens': itens
    }

    return render(request, 'reluci/checklist.html', data)
