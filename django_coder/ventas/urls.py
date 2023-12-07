from django.urls import path
from ventas.views import crear_cliente, leer_clientes, eliminar_cliente, editar_cliente, VentaListView, VentaCreateView, VentaDeleteView, VentaUpdateView, VentaDetailView

urlpatterns = [
    # CRUD de clientes creado con vistas basadas en funciones:
    path('crear_cliente/', crear_cliente, name='crear cliente'),
    path('leer_clientes/', leer_clientes, name='leer clientes'),
    path('eliminar_cliente/<nombre_cliente>', eliminar_cliente, name='eliminar cliente'),
    path('editar_cliente/<nombre_cliente>', editar_cliente, name='editar cliente'),
    # CRUD de ventas creado con vistas basadas en clases:
    path('ventas_lista/', VentaListView.as_view(), name='ventas lista'),
    path('ventas_crear/', VentaCreateView.as_view(), name='ventas crear'),
    # En estas vistas necesitamos agregar un detalle extra que es el argumento <pk>
    # con este argumento que traemos desde el html se identifica cuál es la venta que vamos a acceder.
    path('<pk>/eliminar/', VentaDeleteView.as_view(), name='ventas eliminar'),
    path('<pk>/editar/', VentaUpdateView.as_view(), name='ventas editar'),
    path('<pk>/detalle/', VentaDetailView.as_view(), name='ventas detalle')
]