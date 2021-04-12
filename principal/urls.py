"""configurar urls aqui dentro"""

from django.urls import path
from . import views #importa um arquivo que está no mesmo diretorio

urlpatterns = [
    path('', views.index, name='index')
]