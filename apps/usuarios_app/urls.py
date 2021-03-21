from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('ingresa', views.ingresa, name="ingresa"),
    path('registro', views.registro, name="registro"),
    path('iniciar_sesion', views.iniciar_sesion, name="iniciar_sesion"),
    path('registrar', views.registrar, name="registrar"),
]