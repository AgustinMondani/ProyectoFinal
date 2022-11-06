from django.shortcuts import render
from django.http import HttpResponse
from Blog.forms import ArticuloForm, AutorForm, SeccionForm

def inicio(request):
    return render(request, "formulario_madre.html")


def formularion_autor(request):
    formulario = AutorForm()
    contexto = {"formulario" : formulario}
    return render(request, "formulario_autor.html", context = contexto)


def formulario_articulo(request):
    formulario = ArticuloForm()
    contexto = {"formulario" : formulario}
    return render(request, "formulario_articulo.html", context = contexto)


def formulario_seccion(request):
    formulario = SeccionForm()
    contexto = {"formulario" : formulario}
    return render(request, "formulario_seccion.html", context = contexto)
