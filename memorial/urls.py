from django.urls import path
from memorial.views import index, help, about

#criado para não floodar o setting url com todas as urls do site, separar por app

urlpatterns = [
    path('', index, name='index'),
    path('ajuda', help, name='ajuda'),
    path('sobre', about, name='sobre'),
]