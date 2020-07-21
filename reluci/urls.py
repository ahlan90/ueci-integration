from django.urls import path

from . import views
from .views import FolhaTrabalhoPrintView

urlpatterns = [
    path('reluci', views.checklist_reluci, name='checklist_reluci'),
    path('relato/<int:pk>', views.relato_ponto_controle, name='relato_ponto_controle'),
    path('ponto-controle/<int:pk>', views.ponto_controle_detail, name='ponto_controle_detail'),
    path('ponto-controle2/<int:pk>', views.ponto_controle_detail2, name='ponto_controle_detail2'),
    path('ponto-controle/criar/<int:pk>', views.analise_ponto_controle_create, name='analise_ponto_controle_create'),
    path('ponto-controle/atualizar/<int:pk>', views.analise_ponto_controle_update, name='analise_ponto_controle_update'),
    path('folha-trabalho/<int:pk>', FolhaTrabalhoPrintView.as_view(), name='folha_trabalho_pdf'),

    path('ponto-controle/analise/<int:pk>', views.ponto_controle_detail_analise, name='ponto_controle_detail_analise'),

    path('observacao-tarefa/criar/<int:pk>', views.observacao_tarefa_create, name='observacao_tarefa_create'),
    path('observacao-tarefa/atualizar/<int:pk>', views.observacao_tarefa_update, name='observacao_tarefa_update'),

]
