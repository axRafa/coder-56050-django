from django.contrib import admin

# Register your models here.

from stock.models import Insumo, Producto

admin.site.register(Insumo)
admin.site.register(Producto)