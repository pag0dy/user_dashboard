from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=150)
    clave = models.CharField(max_length=80)
    admin = models.BooleanField()

    def __str__(self):
        return self.correo

