from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import (
    Post,
    Categoria,
    Autor
)

def home(request):
    post = Post.objects.filter(estado=True)
    return render(request, 'index.html', {'posts': post})

def detallePost(request, slug):
    # post = Post.objects.filter(slug=slug).first()
    post = get_object_or_404(Post , slug=slug)
    return render(request, 'post.html', {'detalle_post': post})

def generales(request):
    post = Post.objects.filter(estado=True, categoria= Categoria.objects.filter(nombre__iexact='Generales').first())
    return render(request, 'generales.html', {'posts': post})

def programacion(request):
    post = Post.objects.filter(estado=True, categoria= Categoria.objects.filter(nombre__iexact='Programación').first())
    return render(request, 'programacion.html', {'posts': post})

def contacto(request):
    post = Post.objects.filter(estado=True, categoria= Categoria.objects.filter(nombre__iexact='Contacto').first())
    return render(request, 'contacto.html', {'posts': post})

def careers(request):
    post = Post.objects.filter(estado=True, categoria=Categoria.objects.filter(nombre__iexact='Careers').first())
    return render(request, 'careers.html', {'posts':post})