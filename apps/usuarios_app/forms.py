from django import forms
from .models import Usuario

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['admin', 'desc']

        widgets = {
            "clave" : forms.PasswordInput(),
            "confirma_clave" : forms.PasswordInput()
        }

        labels = {
            'confirma_clave' : 'Confirma tu clave'
        }

        error_messages = {
            'nombre': {
                'max_length': 'El nombre no puede tener más de 100 caracteres',
                'required' : 'Debes ingresar tu nombre'
            },
            'apellido': {
                'max_length': 'El apellido no puede tener más de 100 caracteres',
                'required' : 'Debes ingresar tu apellido'
            },
            'correo': {
                'invalid': 'Por favor ingresa un correo válido',
                'required': 'Debes ingresar tu correro'
            }
        }