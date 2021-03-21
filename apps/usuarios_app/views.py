from django.shortcuts import render, redirect, HttpResponse

def inicio(request):
    return render(request, 'inicio.html')

def ingresa(request):
    return render(request, 'ingreso.html')

def registro(request):
    return render(request, 'registro.html')

def iniciar_sesion(request):
    return HttpResponse('Iniciar sesión')

def registrar(request):
    return HttpResponse('Registrar')

