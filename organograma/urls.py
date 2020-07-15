from django.urls import path

from . import views
from .views import Organograma

urlpatterns = [
    path('', Organograma.as_view(), name='organograma'),
]