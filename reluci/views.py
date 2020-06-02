from django.shortcuts import render

# Create your views here.
from reluci.models import ItensPontoControle


def checklist_reluci(request):

    itens = ItensPontoControle.objects.all()

    data = {
        'itens': itens
    }

    return render(request, 'reluci/checklist.html', data)
