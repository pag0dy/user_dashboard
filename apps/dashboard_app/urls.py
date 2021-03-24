from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.muro, name='muro'),
    path('usuario', views.perfil_usuario, name='perfil_usuario'),
    path('panel', views.panel, name='panel'),
    path('mensaje', views.mensaje, name='mensaje')
]