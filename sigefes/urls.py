from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('despesa-liquidada-file', views.despesa_liquidada_upload, name='despesa-liquidada-file'),
]