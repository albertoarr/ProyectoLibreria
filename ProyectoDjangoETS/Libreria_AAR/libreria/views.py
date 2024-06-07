from django.shortcuts import render
from django.http import Http404
from .models import Autor, Libro


# Create your views here.

def index(request):
    template_a = Autor.objects.order_by("id")
    context = {
        "template_a": template_a
    }
    return render(request, "index.html", context)

def libros_autor(request, autor_id):
    try:
        libros = Libro.objects.filter(autor=autor_id)
    except Autor.DoesNotExist:
        raise Http404("El autor no tiene libros registrados")
    context = {
        "libros" : libros
    }
    return render(request, "libros_autor.html", context)

def datos_libro(request, libro_id):
    try:
        datos = Libro.objects.get(id=libro_id)
    except Libro.DoesNotExist:
        raise Http404("El autor no tiene libros registrados")
    
    context = {
        "datos" : datos
    }

    return render(request, "datos_libro.html", context)

