from django.shortcuts import render, redirect, HttpResponse
from ..usuarios_app.models import Usuario
from .models import Mensaje

def muro(request, id):
    este_usuario = Usuario.objects.filter(id=id)[0]

    return render(request, 'muro.html', {'este_usuario': este_usuario})

def perfil_usuario(request):
    if request.method == 'GET':
        if 'usuario' in request.session:
            este_usuario = Usuario.objects.filter(id=request.session['usuario'])[0]

        return render(request, 'perfil_usuario.html', {'este_usuario': este_usuario})
    
    else: 
        return HttpResponse('hola')


def panel(request):
    if 'usuario' in request.session:
        usuarios = Usuario.objects.all()
        return render(request, 'panel.html', {'usuarios':usuarios})
    else:
        return HttpResponse('No has iniciado sesión')

def mensaje(request):
    if 'usuario' in request.session:
        print(request.POST)
        id_muro = request.POST['id_usuario_muro'][0]
        recibe = Usuario.objects.filter(id=id_muro)[0]
        envia = Usuario.objects.filter(id=request.session['usuario'])[0]
        mensaje = Mensaje.objects.create(contenido=request.POST['mensaje'], creado_por=envia, enviado_a=recibe)
        return redirect('' + str(id_muro))