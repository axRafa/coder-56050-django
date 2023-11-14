from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    nro_cuit = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre + ", CUIT: " + str(self.nro_cuit)

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ventas")
    nro_transaccion = models.IntegerField()
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha_de_venta = models.DateField()
    
    def __str__(self):
        return "Venta nro: " + str(self.nro_transaccion)