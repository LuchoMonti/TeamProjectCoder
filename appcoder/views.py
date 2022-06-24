from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Titulo Pagina</h1>')

def un_template(request):
    return HttpResponse('<h1>Mi Template</h1>')