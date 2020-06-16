from django.urls import path

from . import views

urlpatterns = [
    path('reluci', views.checklist_reluci, name='checklist_reluci'),
    path('relato/<int:pk>', views.relato_ponto_controle, name='relato_ponto_controle'),
    path('ponto-controle/criar/<int:pk>', views.analise_ponto_controle_create, name='analise_ponto_controle_create'),
    path('ponto-controle/<int:pk>', views.ponto_controle_detail, name='ponto_controle_detail'),
    path('ponto-controle/atualizar/<int:pk>', views.analise_ponto_controle_update, name='analise_ponto_controle_update'),
]