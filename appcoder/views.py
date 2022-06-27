from mailbox import NoSuchMailboxError
from django import template
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Prueba

# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Titulo Pagina</h1>')

def un_template(request):
    
    # template = loader.get_template('index.html')
    
    prueba1 = Prueba(nombre='primero')
    prueba2 = Prueba(nombre='segundo')
    prueba3 = Prueba(nombre='tercero')
    prueba1.save()
    prueba2.save()
    prueba3.save()
    
    # render = template.render({'lista_objeto': [prueba1, prueba2, prueba3]})
    
    return render(request, 'index.html', {'lista_objeto': [prueba1, prueba2, prueba3]})
    
    return HttpResponse(render)