import json

from django.http import HttpResponse
from django.shortcuts import render
from Busca.models import Pessoa


def autocompleteModel(request):
    if request.is_ajax():
        #pegando o nome digitado no post
        nome_pessoa = request.GET.get('term', '').capitalize()

        #pegando o objeto cujo nome é o digitado no post e usa o "startswith" para exibir
        pessoa = Pessoa.objects.filter(nome__startswith=nome_pessoa)

        resultado = []
        for r in pessoa:
            resultado.append(r.nome)
        data = json.dumps(resultado)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def Index(request):
    return render(request, 'index.html', locals())
