from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render,redirect
import random
from .models import Usuario
from .forms import CrearUsuarioFormulario, BuscarUsuario


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

#VERSION 1
# def crear_usuario(request):
#     print(f'valor de request',request)
#     print(f'valor de GET',request.GET)
#     print(f'valor de POST',request.POST)
    
    
#     if request.method == "POST":
#         usuario = Usuario(nombre = request.POST.get('nombre'),apellido=request.POST.get('apellido') , correo=request.POST.get('correo'))
#         usuario.save()
    
#     return render(request,"inicio/crear_usuario.html")

def crear_usuario(request):
    if request.method == 'POST':
        formulario = CrearUsuarioFormulario(request.POST)
        if formulario.is_valid():
                datos = formulario.cleaned_data
                print('&&&&&&&&&&&&& DATOS DE USUARIO:',datos)
                usuario = Usuario(nombre=datos.get("nombre"),apellido=datos.get('apellido'),correo=datos.get('correo'))
                usuario.save()
                return redirect('bienvenido')
    else: #es GET
        formulario = CrearUsuarioFormulario()  
    return render(request,"inicio/crear_usuario.html", {'formulario':formulario})

def bienvenido(request):
    print('&&&&&&&&&&&&& DATOS DE USUARIO:',request)
    
    formulariobuscar = BuscarUsuario(request.GET)
    if formulariobuscar.is_valid():
        nombre = formulariobuscar.cleaned_data['nombre']
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
    
    # usuarios = Usuario.objects.all()
    return render(request,'inicio/bienvenido.html',{'usuarios':usuarios, 'formulariobuscar':formulariobuscar})

def catalogo(request):
    ...
    
def eliminar_usuario(request):
    return redirect('bienvenido')