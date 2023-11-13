from django.shortcuts import render
from stock.models import Insumo, Producto
from django.template import loader
from django.http import HttpResponse


# Create your views here.

def crear_insumo(request):
    insumo = Insumo(nombre="Tornillo", descripcion="Tipo Alen", cantidad_en_stock=567)
    
    insumo.save()
    
    template = loader.get_template("creacion_insumo.html")
    
    doc = template.render({"nombre": insumo.nombre})
    
    return HttpResponse(doc)