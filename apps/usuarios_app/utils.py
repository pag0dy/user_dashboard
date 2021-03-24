from __future__ import unicode_literals
from django.db import models
import bcrypt

errors = {}

def existe(x, tipo):
    if len(x) == 0:
        errors[tipo] = f'El campo {tipo} es requerido'
    else:
        pass

def mayor_que(x, y, tipo):
    if len(x) < y:
        errors[tipo] = f'El campo {tipo} debe tener al menos {y} caracteres'
    else:
        pass

def solo_letras(x, tipo):
    if str.isalpha(x):
        pass
    else:
        errors[tipo] = f'El campo {tipo} debe contener sólo letras'

def solo_reg(reg, x, tipo):
    if not reg.match(x):
        errors[tipo] = f'El valor ingresado en {tipo} no es válido'
    else:
        pass

def iguales(x, y, tipo):
    if x != y:
        errors[tipo] = f'Los valores ingresados en {tipo} no coinciden'
    else:
        pass
