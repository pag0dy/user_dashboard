from django.db import models
from ..usuarios_app.models import Usuario

class Mensaje(models.Model):
    contenido = models.TextField()
    creado_por = models.ForeignKey(Usuario, related_name='mensajes_enviados', on_delete=models.CASCADE)
    enviado_a = models.ForeignKey(Usuario, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contenido
    
class Comentarios(models.Model):
    contenido = models.TextField()
    creado_por = models.ForeignKey(Usuario, related_name='comentario_enviado', on_delete=models.CASCADE)
    mensaje_comentado = models.ForeignKey(Mensaje, related_name='comentarios', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.contenido