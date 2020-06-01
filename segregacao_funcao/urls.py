from django.urls import path

from . import views

urlpatterns = [
    path('segregacao-funcao', views.contribuicao_patronal_upload, name='segregacao-funcao'),
]