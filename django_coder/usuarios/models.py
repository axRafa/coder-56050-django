from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    CHOICE = (
        ('cliente', 'cliente'),
        ('vendedor', 'vendedor')
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    imagen = models.ImageField(upload_to='imagenes_usuarios')
    rol = models.CharField(max_length=10, choices=CHOICE, null=True, blank=True)
    
    def __str__(self):
        return "Usuario: " + self.usuario.username + ", Rol del usuario: " + str(self.rol)