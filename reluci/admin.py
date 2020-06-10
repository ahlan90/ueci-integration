from django.contrib import admin

from reluci.models import ItemGestao, PontoControle, Atividade, ItemAbordagem, Tarefa, SubPontoControle, \
    AnalisePontoControle, AnaliseSubPontoControle

admin.site.register(ItemAbordagem)
admin.site.register(ItemGestao)
admin.site.register(PontoControle)
admin.site.register(SubPontoControle)
admin.site.register(Tarefa)
admin.site.register(Atividade)


admin.site.register(AnalisePontoControle)
admin.site.register(AnaliseSubPontoControle)

