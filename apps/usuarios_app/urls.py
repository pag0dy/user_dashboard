from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('ingresa', views.ingresa, name="ingresa"),
    path('registro', views.registro, name="registro"),
    path('salir', views.salir, name="salir"),
]
