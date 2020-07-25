from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)
#from . models import Libros


#Create your views here.
class IndexView(TemplateView):
    # Una vista procesa los datos y renderiza el resultado en pantalla
    # Siempre nos pedira un template con el que trabajar.#
    template_name="home/index.html"

class ListaLibros(ListView):
    template_name="home/index.html"
    queryset=['El quijote','Codigo Limpio','Django puro']
    context_object_name='libros'


  