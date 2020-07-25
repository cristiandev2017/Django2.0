from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Autor, Libros, Categoria

#Clase para mejorar la vista del administrador
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'Nombre',
        'Nacionalidad',
        'id'
    )

    #Atributo para buscar por campos
    search_fields = ('Nombre', 'Nacionalidad',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'Nombre',
        'Resumen',
        'id'
    )

    #Atributo para buscar por campos
    search_fields = ('Nombre',)

class LibroAdmin(admin.ModelAdmin):
    list_display = (
        'Isbn',
        'Titulo',
        'Resumen',
        'Autor',
        'Categoria',
        'id'
    )

    #Atributo para buscar por campos
    search_fields = ('Titulo',)


admin.site.register(Autor,AutorAdmin)
admin.site.register(Libros,LibroAdmin)
admin.site.register(Categoria,CategoriaAdmin)
