from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('posts/', views.posts, name='posts'),
    path('autors/', views.autors, name='autors'),
    path('categorias/', views.categorias, name='categorias'),
    path('postsApi/', views.postsapi),
    path('busquedaPost/', views.buscarpost, name='buscarpost'),
    path('buscar/', views.buscar),
    path('posts/list/', views.PostList.as_view(), name="List"),
    path('posts/edit/<pk>', views.PostEdit.as_view(), name="Edit"),
    path('posts/create/', views.PostCreate.as_view(), name="New"),
    path('posts/detail/<pk>', views.PostDetail.as_view(), name="Detail"),
    path('posts/delete/<pk>', views.PostDelete.as_view(), name="Delete"),
    path('busquedaAutor/', views.buscarautor, name='buscarautor'),
    path('autor/list/', views.AutorList.as_view(), name="Listautor"),
    path('autor/edit/<pk>', views.AutorEdit.as_view(), name="Editautor"),
    path('autor/create/', views.AutorCreate.as_view(), name="Newautor"),
    path('autor/detail/<pk>', views.AutorDetail.as_view(), name="Detailautor"),
    path('autor/delete/<pk>', views.AutorDelete.as_view(), name="Deleteautor"),
    path('buscar2/', views.buscar2),
    path('busquedaCategoria/', views.buscarcategoria, name='buscarcategoria'),
    path('categoria/list/', views.CategoriaList.as_view(), name="Listcategoria"),
    path('categoria/edit/<pk>', views.CategoriaEdit.as_view(), name="Editcategoria"),
    path('categoria/create/', views.CategoriaCreate.as_view(), name="Newcategoria"),
    path('categoria/detail/<pk>', views.CategoriaDetail.as_view(), name="Detailcategoria"),
    path('categoria/delete/<pk>', views.CategoriaDelete.as_view(), name="Deletecategoria"),
    path('buscar3/', views.buscar3),
   
]

