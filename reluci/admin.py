from django.contrib import admin

from reluci.models import GrupoPontoControle, PontoControle, Atividade, ItensPontoControle

admin.site.register(ItensPontoControle)
admin.site.register(GrupoPontoControle)
admin.site.register(PontoControle)
admin.site.register(Atividade)