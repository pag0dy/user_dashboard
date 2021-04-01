from django import forms
from .models import Usuario

class UserForm(forms.ModelForm):

    clave_rep = forms.CharField(max_length=80, label="Confirmar clave")

    class Meta:
        model = Usuario
        exclude = ['desc', 'admin']

        widgets = {
            "clave" : forms.PasswordInput(),
            'clave_rep': forms.PasswordInput(),
        }


class EditOtroForm(forms.ModelForm):

    clave_rep = forms.CharField(max_length=80, label="Confirmar clave")

    class Meta:
        model = Usuario
        fields = '__all__'

        widgets = {
            "clave" : forms.PasswordInput(),
            'clave_rep': forms.PasswordInput()
        }