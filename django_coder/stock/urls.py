from django.urls import path
from stock.views import crear_insumo, crear_producto, busqueda_en_bd, comprar_producto

urlpatterns = [
    path('crear_insumo/', crear_insumo, name='crear insumo'),
    path('crear_producto/', crear_producto, name='crear producto'),
    path('busqueda_bd/', busqueda_en_bd, name='busqueda en bd'),
    path('comprar_producto/', comprar_producto, name='comprar producto'),
]