from django.shortcuts import render

from core.models import Produto

def index(request):
    produtos = Produto.objects.all()

    context = {
        'produtos': produtos
    }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    print(f' PK: {pk}')
    return render( request, 'produto.html')