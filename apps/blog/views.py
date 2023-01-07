from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import (
    Post,
    Categoria,
    Autor
)

def home(request):
    queryset = request.GET.get('buscar')

    # Search bar
    post = Post.objects.filter(estado=True)
    if queryset:
        post = Post.objects.filter(Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset)).distinct()
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'index.html', {'posts': post})

def detallePost(request, slug):
    # post = Post.objects.filter(slug=slug).first()
    post = get_object_or_404(Post , slug=slug)
    return render(request, 'post.html', {'detalle_post': post})

def generales(request):
    queryset = request.GET.get('buscar')

    # Search bar
    post = Post.objects.filter(estado=True, categoria=Categoria.objects.filter(nombre__iexact='Generales').first())
    if queryset:
        post = Post.objects.filter(Q(estado=True) & Q(categoria=Categoria.objects.filter(nombre__iexact='Generales').first()) & (Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset))).distinct()
    
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'generales.html', {'posts': post})

def programacion(request):
    queryset = request.GET.get('buscar')
    
    # Search bar
    post = Post.objects.filter(estado=True, categoria= Categoria.objects.filter(nombre__iexact='Programación').first())
    if queryset:
        post = Post.objects.filter(Q(estado=True) & Q(categoria=Categoria.objects.filter(nombre__iexact='Programación').first()) & (Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset))).distinct()
    
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'programacion.html', {'posts': post})

def contacto(request):
    queryset = request.GET.get('buscar')
    
    # Search bar
    post = Post.objects.filter(estado=True, categoria= Categoria.objects.filter(nombre__iexact='Contacto').first())
    if queryset:
        post = Post.objects.filter(Q(estado=True) & Q(categoria=Categoria.objects.filter(nombre__iexact='Contacto').first()) & (Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset))).distinct()
    
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'contacto.html', {'posts': post})

def careers(request):
    queryset = request.GET.get('buscar')
    
    # Search bar
    post = Post.objects.filter(estado=True, categoria=Categoria.objects.filter(nombre__iexact='Careers').first())
    if queryset:
        post = Post.objects.filter(Q(estado=True) & Q(categoria=Categoria.objects.filter(nombre__iexact='Careers').first()) & (Q(titulo__icontains=queryset) | Q(descripcion__icontains=queryset))).distinct()
    
    paginator = Paginator(post, 2)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'careers.html', {'posts':post})