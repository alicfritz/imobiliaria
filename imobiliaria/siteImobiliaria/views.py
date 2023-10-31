from django.shortcuts import render, HttpResponse
from . models import Imoveis

# Create your views here.

def index(request):
    return HttpResponse('<h2>teste<h2>')

def lista_imoveis(request):
    imoveis = Imoveis.objects.all()
    return render(request, 'lista_imoveis.html', {'imoveis': imoveis})