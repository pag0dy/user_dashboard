from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from ..usuarios_app.models import Usuario
from ..usuarios_app.forms import UserForm, EditOtroForm
from .models import Mensaje, Comentarios
import bcrypt

def filtro_usuario(id_usuario):
    activo = Usuario.objects.filter(id = id_usuario)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo
    else:
        mensaje = 'No se encontró el usuario'
        print(mensaje)
        return mensaje


def muro(request, id_usuario):
    if 'este_usuario' in request.session:
        este_usuario = filtro_usuario(request.session['este_usuario'])
        muro_usuario = filtro_usuario(id_usuario)
        mensajes = muro_usuario.mensajes_recibidos.all().order_by('-created_at')
        context = {
            'este_usuario' : este_usuario,
            'muro_usuario' : muro_usuario,
            'mensajes' : mensajes
        }
        return render(request, 'muro.html', context)


def perfil_usuario(request):
    if request.method == 'GET':
        if 'este_usuario' in request.session:
            try:
                este_usuario = filtro_usuario(request.session['este_usuario'])
                context = {
                    'este_usuario': este_usuario,
                    'otro_usuario' : este_usuario
                }

                return render(request, 'perfil_usuario.html', context)
            except:
                mensaje = 'No has inciado sesión'
                messages.error(request, mensaje)
                return HttpResponse('hola')

    else:
        if 'id_otro_usuario' in request.POST:
            print(request.POST)
            este_usuario = filtro_usuario(request.session['este_usuario'])
            otro_usuario = filtro_usuario(request.POST['id_otro_usuario'])
            context = {
                'este_usuario': este_usuario, 
                'otro_usuario': otro_usuario
            }
            return render(request, 'perfil_usuario.html', context)
    

def editar_usuario(request):
    if request.method == 'POST':
        if 'este_usuario' in request.session:
                if 'id_otro_usuario' in request.POST:
                    usuario_a_editar = filtro_usuario(request.POST['id_otro_usuario'])
                    errors = Usuario.objects.validar_edicion_info(request.POST)
                    if len(errors) > 0:
                        for key, value in errors.items():
                            messages.error(request, value)
                        
                        return redirect('panel')
                    else:
                        usuario_a_editar.nombre = request.POST['nombre_usuario']
                        usuario_a_editar.apellido = request.POST['apellido_usuario']
                        usuario_a_editar.correo = request.POST['correo_usuario']
                        usuario_a_editar.save()
                        mensaje = "Información actualizada!"
                        messages.success(request, mensaje)
                        return redirect('panel')
        
        else:
            return HttpResponse('No puedes acceder a estas funciones')


def editar_clave(request):
    if request.method == 'POST':
        print(request.POST)
        if 'este_usuario' in request.session:
            if 'id_otro_usuario' in request.POST:
                usuario_a_editar = filtro_usuario(request.POST['id_otro_usuario'])
                errors = Usuario.objects.validar_cambio_clave(request.POST)

                if len(errors) > 0 :
                        for key, value in errors.items():
                            messages.error(request, value)

                        return redirect('panel')

                else:
                    clave = request.POST['clave_usuario']
                    pw_hash = bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()
                    usuario_a_editar.clave = pw_hash
                    usuario_a_editar.save()
                    mensaje = "Clave actualizada!"
                    messages.success(request, mensaje)
                    return redirect('panel')

            return HttpResponse('No puedes acceder a estas funciones')


def editar_desc(request):
    print(request.POST)
    if request.method == 'POST':
        if 'este_usuario' in request.session:
            if 'id_otro_usuario' in request.POST:
                usuario_a_editar = filtro_usuario(request.POST['id_otro_usuario'])
                usuario_a_editar.desc = request.POST['desc_usuario']
                usuario_a_editar.save()
                mensaje = "Descripción actualizada!"
                messages.success(request, mensaje)
                return redirect('panel')
    else:

        return HttpResponse('No puedes acceder a estas funciones')


def editar_admin(request):
    if request.method == 'POST':
        if 'este_usuario' in request.session:
            if 'id_otro_usuario' in request.POST:
                usuario_a_editar = filtro_usuario(request.POST['id_otro_usuario'])
                usuario_a_editar.admin = request.POST['admin_usuario']
                usuario_a_editar.save()
                mensaje = "Nivel de permisos actualizada!"
                messages.success(request, mensaje)
                return redirect('panel')
    else:

        return HttpResponse('No puedes acceder a estas funciones')


def eliminar_usuario(request):
    if 'este_usuario' in request.session:
        este_usuario = filtro_usuario(request.session['este_usuario'])
        otro_usuario = filtro_usuario(request.POST['id_otro_usuario'])
        otro_usuario.delete()
        return redirect('panel')
    else:
        return HttpResponse('No puedes acceder a estas funciones')


def agregar(request):
    if 'este_usuario' in request.session:
        if request.method == 'POST':

                errors = Usuario.objects.validar_registro(request.POST)

                if len(errors) > 0 :
                    for key, value in errors.items():
                        messages.error(request, value)

                    return redirect('panel')

                else:
                    clave = request.POST['clave']
                    pw_hash = bcrypt.hashpw(clave.encode(), bcrypt.gensalt()).decode()
                    if not Usuario.objects.all():
                        admin = True
                    else:
                        admin = False
                    usuario = Usuario.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'], correo=request.POST['correo'], clave=pw_hash, admin=admin)
                    mensaje = 'Nuevo usuario creado!'
                    messages.success(request, mensaje)

                    return redirect('panel')
        else:
            return render(request, 'agregar.html')    


def panel(request):
    if 'este_usuario' in request.session:
        este_usuario = filtro_usuario(request.session['este_usuario'])
        usuarios = Usuario.objects.all()
        context = {
            'este_usuario' : este_usuario,
            'usuarios' : usuarios
        }
        return render(request, 'panel.html', context)
    else:
        return HttpResponse('No has iniciado sesión')


def mensaje(request):
    if 'este_usuario' in request.session:
        print(request.POST)
        recibe = filtro_usuario(request.POST['id_usuario_muro'])
        envia = filtro_usuario(request.session['este_usuario'])
        mensaje = Mensaje.objects.create(contenido=request.POST['mensaje'], creado_por=envia, enviado_a=recibe)
        return redirect('muro/' + str(request.POST['id_usuario_muro']))


def comentario(request):
    if 'este_usuario' in request.session:
        print(request.POST)
        recibe = filtro_usuario(request.POST['id_usuario_muro'])
        envia = filtro_usuario(request.session['este_usuario'])
        mensaje = Mensaje.objects.filter(id=request.POST['id_mensaje'])[0]
        comentario = Comentarios.objects.create(contenido=request.POST['comentario'], mensaje_comentado=mensaje, creado_por=envia)
        return redirect('muro/' + str(request.POST['id_usuario_muro']))