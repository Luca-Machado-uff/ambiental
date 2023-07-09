from django.shortcuts import render, get_object_or_404
from memorial.models import Memorias

def index(request):
    memorias = Memorias.objects.order_by("ano_de_falecimento", "nome")

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            memorias = memorias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'memorial/index.html', {"nomes": memorias})

def about(request):
    return render(request, 'memorial/about.html')

def help(request):
    return render(request, 'memorial/help.html')


def individual(request, _id):
    memoria = get_object_or_404(Memorias, pk=_id)
    return render(request, 'memorial/individual.html', {"memoria": memoria})