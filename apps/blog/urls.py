from django.urls import path
from .views import (
    home,
    generales,
    programacion,
    contacto,
    detallePost,
    careers
)

urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales, name='generales'),
    path('programacion/', programacion, name='programacion'),
    path('contacto/', contacto, name='contacto'),
    path('careers/', careers, name='careers'),
    path('<slug:slug>/', detallePost, name='detalle-post'),

]