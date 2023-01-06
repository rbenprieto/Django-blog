from django.shortcuts import render
from .models import (
    Post,
    Categoria,
    Autor
)

def home(request):
    post = Post.objects.filter(estado=True)
    return render(request, 'index.html', {'posts': post})


def generales(request):
    post = Post.objects.filter(estado=True, categoria= Categoria.objects.filter(nombre='Generales').first())
    return render(request, 'generales.html', {'posts': post})

def programacion(request):
    post = Post.objects.filter(estado=True, categoria= Categoria.objects.filter(nombre='Programación').first())
    return render(request, 'programacion.html', {'posts': post})

def contacto(request):
    post = Post.objects.filter(estado=True, categoria= Categoria.objects.filter(nombre='Contacto').first())
    return render(request, 'contacto.html', {'posts': post})
