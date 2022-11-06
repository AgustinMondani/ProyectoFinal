from django.shortcuts import render
from django.http import HttpResponse
from Blog.forms import ArticuloForm, AutorForm, SeccionForm
from Blog.models import Articulo, Seccion, Autor

def inicio(request):
    return render(request, "formulario_madre.html")


def formularion_autor(request):

    if request.method == "GET":
        formulario = AutorForm()
        contexto = {"formulario" : formulario}
        return render(request, "formulario_autor.html", context = contexto)

    if request.method == "POST":
        formulario = AutorForm(request.POST)
        if formulario.is_valid():
            datos_ingreasados = formulario.cleaned_data
            nuevo_modelo = Autor(
                nombre = datos_ingreasados["nombre"],
                apellido = datos_ingreasados["apellido"],
                edad = datos_ingreasados["edad"],
                especialidad = datos_ingreasados["especialidad"],
            )
        nuevo_modelo.save()
    contexto = {"formulario" : formulario}
    return render(request, "formulario_exitoso.html", context = contexto)



def formulario_articulo(request):

    if request.method == "GET":
        formulario = ArticuloForm()
        contexto = {"formulario" : formulario}
        return render(request, "formulario_articulo.html", context = contexto)

    if request.method == "POST":
        formulario = ArticuloForm(request.POST)
        if formulario.is_valid():
            datos_ingreasados = formulario.cleaned_data
            nuevo_modelo = Articulo(
                titulo = datos_ingreasados["titulo"],
                texto = datos_ingreasados["texto"],
                fecha = datos_ingreasados["fecha"],
            )
            nuevo_modelo.save()
    contexto = {"formulario" : formulario}
    return render(request, "formulario_exitoso.html", context = contexto)


def formulario_seccion(request):

    if request.method == "GET":
        formulario = SeccionForm()
        contexto = {"formulario" : formulario}
        return render(request, "formulario_seccion.html", context = contexto)

    if request.method == "POST":
        formulario = SeccionForm(request.POST)
        if formulario.is_valid():
            datos_ingreasados = formulario.cleaned_data
            nuevo_modelo = Seccion(
                nombre = datos_ingreasados["nombre"],
            )
            nuevo_modelo.save()
    contexto = {"formulario" : formulario}
    return render(request, "formulario_exitoso.html", context = contexto)

def buscar(request):

    if request.method == "GET":
        return render(request, "formulario_busqueda.html")

    if request.method == "POST":
        contexto = {}
        return render(request, "resultado_busqueda.html", context = contexto)