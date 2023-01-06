from django.urls import path
from .views import (
    home,
    generales,
    programacion,
    contacto
)

urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales, name='generales'),
    path('programacion/', programacion, name='programacion'),
    path('contacto/', contacto, name='contacto'),

]