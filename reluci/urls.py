from django.urls import path

from . import views

urlpatterns = [
    path('reluci', views.checklist_reluci, name='checklist_reluci'),
    path('relato/<int:pk>', views.relato_ponto_controle, name='relato_ponto_controle'),
]