from django import forms

class PostFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    contenido = forms.CharField(max_length=200)

class AutorFormulario(forms.Form):
    nombre_autor = forms.CharField(max_length=40)
    nacionalidad_autor = forms.CharField(max_length=40)

class CategoriaFormulario(forms.Form):
    nombre_categoria = forms.CharField(max_length=40)    


