from django.contrib import admin
from apps.blog.models import (
    Autor,
    Categoria,
    Post
)
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria
        
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion')
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'email']
    list_display = ('nombres', 'apellidos', 'estado')
    list_display_links = list_display
    resource_class = AutorResource

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)