from django.contrib import admin

# Register your models here.
from sigefes.models import *

admin.site.register(UnidadeGestora)
admin.site.register(Credor)
admin.site.register(Processo)
admin.site.register(Despesa)
admin.site.register(DespesaLiquidada)
admin.site.register(DespesaEmpenhada)
admin.site.register(NotaLiquidacao)
