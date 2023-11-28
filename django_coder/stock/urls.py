from django.urls import path
from stock.views import crear_insumo, crear_producto

urlpatterns = [
    path('crear_insumo/', crear_insumo, name='crear_insumo'),
    path('crear_producto/', crear_producto, name='crear producto'),
]