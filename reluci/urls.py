from django.urls import path

from . import views

urlpatterns = [
    path('reluci', views.checklist_reluci, name='checklist_reluci'),
]