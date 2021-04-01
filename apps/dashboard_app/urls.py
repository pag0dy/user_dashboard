from django.urls import path
from . import views

urlpatterns = [
    path('muro/<int:id_usuario>', views.muro, name='muro'),
    path('usuario', views.perfil_usuario, name='perfil_usuario'),
    path('panel', views.panel, name='panel'),
    path('mensaje', views.mensaje, name='mensaje'),
    path('comentario', views.comentario, name='comentario'),
    path('agregar', views.agregar, name='agregar'),
    path('editar_usuario', views.editar_usuario, name='editar_usuario'),
    path('editar_clave', views.editar_clave, name='editar_clave'),
    path('editar_desc', views.editar_desc, name='editar_desc'),
    path('editar_admin', views.editar_admin, name='editar_admin'),
    path('eliminar_usuario', views.eliminar_usuario, name='eliminar_usuario'),
]