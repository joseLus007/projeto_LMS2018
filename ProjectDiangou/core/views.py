from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'title': 'E-Commerce FIT',
        'paragrafo1': 'Primeiro parágrafo aqui',
        'paragrafo2': 'Segundo parágrafo aqui',
        'alunos': ['Ricardo','Marco','Marco Chocolate','Kleverson','Predo'],
        'alunos2': [],
        'condicao1': True,
        'condicao2': False,
        'lista': [1,2,3,4,5]
    }
    return render(request,"index.html",context)
def paginalogin (request):
        return render (request,'paginalogin.html')
