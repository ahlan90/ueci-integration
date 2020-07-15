from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from organograma.models import Entidade


class Organograma(ListView):

    queryset = Entidade.objects.all().order_by('-entidade_auditora')
    template_name = 'organograma/organograma.html'
