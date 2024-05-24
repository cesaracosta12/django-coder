from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Hola wachin')

# http://127.0.0.1:8000/