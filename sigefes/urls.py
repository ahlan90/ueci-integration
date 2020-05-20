from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sigefes', views.upload_file, name='sigefes'),
]