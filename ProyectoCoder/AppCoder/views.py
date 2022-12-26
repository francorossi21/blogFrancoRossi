from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Post
from AppCoder.models import Autor
from AppCoder.models import Categoria
from django.core import serializers
from AppCoder.forms import PostFormulario
from AppCoder.forms import AutorFormulario
from AppCoder.forms import CategoriaFormulario

def buscar(request):
    print(request)
    titulo_views = request.GET['titulo']
    posts_todos = Post.objects.filter(titulo=titulo_views)
    return render(request, 'AppCoder/resultadoPost.html', {'titulo':titulo_views, 'posts':posts_todos})

def buscarpost(request):
    return render(request, 'AppCoder/busquedaPost.html')

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def posts(request):
    if request.method == "POST":
        miFormulario = PostFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            post = Post(titulo=informacion["titulo"], contenido=informacion["contenido"])
            post.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = PostFormulario()
    return render(request, "AppCoder/posts.html", {"miFormulario": miFormulario})

def postsapi(request):
    posts_todos = Post.objects.all()
    return HttpResponse(serializers.serialize('json',posts_todos))

def autors(request):
    if request.method == "POST":
        miFormulario = AutorFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            autor = Autor(nombre_autor=informacion["nombre_autor"], nacionalidad_autor=informacion["nacionalidad_autor"])
            autor.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = AutorFormulario()
    return render(request, "AppCoder/autor.html", {"miFormulario": miFormulario})

def categorias(request):
    if request.method == "POST":
        miFormulario = CategoriaFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            categoria = Categoria(nombre_categoria=informacion["nombre_categoria"])
            categoria.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CategoriaFormulario()
    return render(request, "AppCoder/categoria.html", {"miFormulario": miFormulario})  


   
    #def autorsapi(request):
    #autors_todos = Autor.objects.all()
    #return HttpResponse(serializers.serialize('json',autors_todos))

#CRUD - create, read. update, delete
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class PostList(ListView):
    model = Post
    template = 'AppCoder/posts_list.html'

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/AppCoder/posts/list/'

#EDITAR
from django.views.generic.detail import DetailView

class PostEdit(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/AppCoder/posts/list/'

#DETALLE

class PostDetail(DetailView):
    model = Post
    template = 'AppCoder/post_detail.html'

#Borrar

class PostDelete(DeleteView):
    model = Post
    #fields= '__all__'
    success_url= '/AppCoder/posts/list'

class AutorList(ListView):
    model = Autor
    template = 'AppCoder/autor_list.html'

class AutorCreate(CreateView):
    model = Autor
    fields = '__all__'
    success_url = '/AppCoder/autor/list/'

class AutorEdit(UpdateView):
    model = Autor
    fields = '__all__'
    success_url = '/AppCoder/autor/list/'

#DETALLE

class AutorDetail(DetailView):
    model = Autor
    template = 'AppCoder/autor_detail.html'

#Borrar

class AutorDelete(DeleteView):
    model = Autor
    #fields= '__all__'
    success_url= '/AppCoder/autor/list'

def buscarautor(request):
    return render(request, 'AppCoder/busquedaAutor.html')

def buscar2(request):
    print(request)
    nombre_views = request.GET['nombre_autor']
    autors_todos = Autor.objects.filter(nombre_autor=nombre_views)
    return render(request, 'AppCoder/resultadoAutor.html', {'nombre_autor':nombre_views, 'autors':autors_todos})    

###################################################################################

class CategoriaList(ListView):
    model = Categoria
    template = 'AppCoder/categoria_list.html'

class CategoriaCreate(CreateView):
    model = Categoria
    fields = '__all__'
    success_url = '/AppCoder/categoria/list/'

class CategoriaEdit(UpdateView):
    model = Categoria
    fields = '__all__'
    success_url = '/AppCoder/categoria/list/'

#DETALLE

class CategoriaDetail(DetailView):
    model = Categoria
    template = 'AppCoder/categoria_detail.html'

#Borrar

class CategoriaDelete(DeleteView):
    model = Categoria
    #fields= '__all__'
    success_url= '/AppCoder/categoria/list'

def buscarcategoria(request):
    return render(request, 'AppCoder/busquedaCategoria.html')

def categories(request):
    if request.method == "POST":
        miFormulario = CategoriaFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            post = Categoria(nombre_categoria=informacion["nombre_categoria"])
            post.save()
            return render(request, "AppCoder/inicio.html")    

def buscar3(request):
    print(request)
    nombre_views = request.GET['nombre_categoria']
    autors_todos = Autor.objects.filter(nombre_autor=nombre_views)
    return render(request, 'AppCoder/resultadoCategoria.html', {'nombre_categoria':nombre_views, 'autors':autors_todos})  
    