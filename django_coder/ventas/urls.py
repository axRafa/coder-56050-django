from django.urls import path
from ventas.views import crear_cliente, leer_clientes, eliminar_cliente, editar_cliente, VentaListView, VentaCreateView

urlpatterns = [
    path('crear_cliente/', crear_cliente, name='crear cliente'),
    path('leer_clientes/', leer_clientes, name='leer clientes'),
    path('eliminar_cliente/<nombre_cliente>', eliminar_cliente, name='eliminar cliente'),
    path('editar_cliente/<nombre_cliente>', editar_cliente, name='editar cliente'),
    path('ventas_lista/', VentaListView.as_view(), name='ventas lista'),
    path('ventas_crear/', VentaCreateView.as_view(), name='ventas crear'),
    
]