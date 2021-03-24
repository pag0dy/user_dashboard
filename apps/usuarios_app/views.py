from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Usuario
import bcrypt

def inicio(request):
    return render(request, 'inicio.html')

def ingresa(request):
    if request.method == 'GET':

        return render(request, 'ingreso.html')

    else:
        errors = Usuario.objects.validar_inicio(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect('ingresa')

        else:
            usuario = Usuario.objects.filter(correo=request.POST['correo'])

            if usuario:

                inicio_usuario = usuario[0]
                request.session['usuario'] = inicio_usuario.id

                return redirect('dash/' + str(inicio_usuario.id))


def registro(request):
    if request.method == 'GET':
        
        return render(request, 'registro.html')

    else:
        errors = Usuario.objects.validar_registro(request.POST)

        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('registro')

        else:
            clave = request.POST['clave']
            pw_hash = bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()
            if not Usuario.objects.all():
                admin = True
            else:
                admin = False
            usuario = Usuario.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'], correo=request.POST['correo'], clave=pw_hash, admin=admin)
            request.session['usuario'] = usuario.id
            print(usuario.id)

            return redirect('dash/' + str(usuario.id))

def salir(request):
    try:
        del request.session['usuario']
        return redirect('inicio')
    except:
        return HttpResponse('no has iniciado una sesión')