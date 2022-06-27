from mailbox import NoSuchMailboxError
from django import template
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Usuarios

# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Titulo Pagina</h1>')

def un_template(request):
    Usuario1 = Usuarios(nombre='Luciano', edad ='30', fecha_nacimiento ='')
    Usuario1.save()
    
    return render(request, 'index.html', {'lista_objeto': [Usuario1]})
