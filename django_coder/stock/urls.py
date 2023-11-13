from django.urls import path
from stock.views import crear_insumo

urlpatterns = [
    path('crear_insumo', crear_insumo, name='crear_insumo')
]