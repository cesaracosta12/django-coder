from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
import random

def home(request):
    return render(request, 'inicio/index.html')


# http://127.0.0.1:8000/

def template1(request):
    fecha = datetime.now()
    archivoabierto = open(r"C:\Users\Cesar\Documents\Python Coder\proyecto-django\templates\plantilla1.html")
    template = Template(archivoabierto.read())
    archivoabierto.close()
    
    datos = {'fecha': fecha,
             'nombre': 'Cesar',
             'apellido': 'Acosta'}
    
    contexto = Context(datos)
    template_renderizado =template.render(contexto)
        
    return HttpResponse(template_renderizado)

def template3(request):
    fecha = datetime.now()
    
    template = loader.get_template('plantilla2.html')
    
    datos = {'fecha': fecha,
             'nombre': 'Cesar',
             'apellido': 'Acosta'}
    
    template_renderizado =template.render(datos)
        
    return HttpResponse(template_renderizado)

def template4(request):
    fecha = datetime.now()
    
    datos = {'fecha': fecha,
             'nombre': 'Cesar',
             'apellido': 'Acosta'}
    
    return render(request,'plantilla4.html',datos)

def probando(request):
    lista = list(range(500))
    
    numeros = random.choices(lista,k=50)
    
    return render(request,'prueba_if_for.html',{'datos':numeros})