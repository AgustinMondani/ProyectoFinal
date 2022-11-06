from django.contrib import admin
from django.urls import path
from Blog.views import formularion_autor , formulario_articulo, formulario_seccion, inicio

urlpatterns = [
    path("admin/", admin.site.urls),
    path("inicio/", inicio),
    path("autor/",formularion_autor),
    path("articulo/", formulario_articulo),
    path("seccion/", formulario_seccion),
]
