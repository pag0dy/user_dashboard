from __future__ import unicode_literals
import re
from django.db import models
from .utils import *

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validar_registro(self, postData):
        solo_letras(postData['nombre'], 'nombre')
        mayor_que(postData['nombre'], 2, 'nombre')
        existe(postData['nombre'], 'nombre')
        solo_letras(postData['apellido'], 'apellido')
        mayor_que(postData['apellido'], 2, 'apellido')
        existe(postData['apellido'], 'apellido')
        solo_reg(EMAIL_REGEX, postData['correo'], 'correo')
        existe(postData['correo'], 'correo')
        mayor_que(postData['clave'], 8, 'clave')
        iguales(postData['clave'], postData['clave_rep'], 'clave')
        existe(postData['clave'], 'clave')

        return errors

    def validar_inicio(self, postData):
        usuario = Usuario.objects.filter(correo = postData['correo'])
        if len(usuario) == 0:
            errors['no_existe'] = 'El correo ingresado no está registrado'
        else:
            usuario = usuario[0]
            if bcrypt.checkpw(postData['clave'].encode(), usuario.clave.encode()):
                pass
            else:
                errors['clave_erronea'] = 'La clave ingresada no corresponde al usuario'

        return errors

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=150)
    clave = models.CharField(max_length=80)
    desc = models.TextField(blank=True)
    admin = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.correo

