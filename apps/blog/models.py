from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=100, verbose_name='Nombre de la categoría')
    estado = models.BooleanField(default=True, verbose_name='Estado de la categoría')
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Autor(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombres = models.CharField(max_length=255, verbose_name='Nombres del autor')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos del autor')
    facebook = models.URLField(null=True, blank=True, verbose_name='Facebook')
    twitter = models.URLField(null=True, blank=True, verbose_name='twitter')
    instagram = models.URLField(null=True, blank=True, verbose_name='instagram')
    web = models.URLField(null=True, blank=True, verbose_name='web')
    email = models.EmailField(verbose_name='Email del autor')
    estado = models.BooleanField( default=True, verbose_name='Estado del autor')
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')

    def __str__(self):
        return "{0}, {1}".format(self.nombres, self.apellidos)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Post(models.Model):
    id = models.AutoField(primary_key=True, editable=False, verbose_name='Id')
    titulo = models.CharField(max_length=90, verbose_name='Titulo')
    slug = models.CharField(max_length=100, verbose_name='Slug')
    descripcion = models.CharField(max_length=110, verbose_name='Descripción')
    contenido = RichTextField
    imagen = models.URLField(max_length=255, verbose_name='Imagen')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Autor')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True, verbose_name='Publicado/No Publicado')
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return str(self.titulo)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    