from django.db import models

# Create your models here.
class Autor(models.Model):
    Nombre = models.CharField('Nombre',max_length=80)
    Nacionalidad = models.CharField('Nacionalidad',max_length=100)

    def __str__(self):
        return self.Nombre

class Categoria(models.Model):
    Nombre = models.CharField('Nombre',max_length=80)
    Resumen = models.TextField('Resumen',blank=True)

    def __str__(self):
        return self.Nombre

class Libros(models.Model):
    Isbn = models.CharField('Isbn', max_length=50, default='')
    Titulo = models.CharField('Titulo', blank=False, max_length=150)
    Resumen = models.TextField('Resumen', blank=True)
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.Titulo