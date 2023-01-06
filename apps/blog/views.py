from django.shortcuts import render
from .models import (
    Post,
    Categoria,
    Autor
)

def home(request):
    post = Post.objects.filter(estado=True)
    print(post)
    return render(request, 'index.html')


def generales(request):
    return render(request, 'generales.html')

def programacion(request):
    return render(request, 'programacion.html')

def contacto(request):
    return render(request, 'contacto.html')
