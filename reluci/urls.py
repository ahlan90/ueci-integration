from django.urls import path

from . import views

urlpatterns = [
    path('reluci', views.checklist_reluci, name='checklist_reluci'),
    path('relato/<int:pk>', views.relato_ponto_controle, name='relato_ponto_controle'),
    path('ponto-controle/criar/', views.ponto_controle_create, name='ponto_controle_create'),
    path('ponto-controle/atualizar/<int:pk>', views.ponto_controle_update, name='ponto_controle_update'),
]