from django.contrib import admin

from reluci.models import ItemGestao, PontoControle, Atividade, ItemAbordagem

admin.site.register(ItemAbordagem)
admin.site.register(ItemGestao)
admin.site.register(PontoControle)
admin.site.register(Atividade)