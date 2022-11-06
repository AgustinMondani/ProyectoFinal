from socket import fromshare
from django import forms


class AutorForm(forms.Form):
        
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    especialidad = forms.CharField(max_length=40)

class ArticuloForm(forms.Form):
        
    titulo = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=350)
    fecha = forms.DateField()

class SeccionForm(forms.Form):
        
    nombre = forms.CharField(max_length=30)   