from django.shortcuts import render
from stock.models import Insumo, Producto
from stock.forms import InsumoFormulario
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def crear_producto(request): 
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_producto = Producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            cantidad_en_stock = request.POST["cantidad_en_stock"]
        )
        nuevo_producto.save()
        return render(request, "index.html")
    
    return render(request, 'producto_formulario.html')

def crear_insumo(request):
    if request.method == "POST":
        nuevo_formulario = InsumoFormulario(request.POST)
        
        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nuevo_insumo = Insumo(
                    nombre=informacion["nombre"],
                    descripcion=informacion["descripcion"],
                    unidad_de_medida=informacion["unidad_de_medida"],
                    cantidad_en_stock=informacion["cantidad_en_stock"]
                    )
                
            nuevo_insumo.save()
            return render(request, 'index.html')
    else:
        nuevo_formulario = InsumoFormulario()
        return render(request, 'insumo_formulario.html', {"formulario": nuevo_formulario})
    

##################################### Vistas que hicimos en el afterclass ############################################
def busqueda_en_bd(request):
    if request.GET.get("nombre", False): # Uso el método .get() de diccionarios para obtener el nombre que recibo desde el html
                                         # Si dicho nombre no existe en el diccionario, entonces devuelve False y no entra en el if
        busqueda = request.GET["nombre"]
        # Con Producto.objects.filter obtengo una lista de todos los elementos que tengan el nombre que ingresé por el formulario
        # __icontains viene de "if contains", con lo cual en lugar de buscar una coincidencia exacta, va a buscar cualquier elemento
        # que contenga el texto que ingresamos en la búsqueda.
        lista_productos = Producto.objects.filter(nombre__icontains=busqueda)
        
        return render(request, 'busqueda.html', {'lista': lista_productos})
    
    return render(request, 'busqueda.html')

def comprar_producto(request):
    # En esta vista estamos buscando un producto en específico y al comprarlo vamos a descontar la cantidad comprada
    # del stock.
    if request.method == "POST":
        busqueda = request.POST["nombre"]
        producto = Producto.objects.get(nombre=busqueda)
        cantidad_compra = int(request.POST["cantidad"])
        # Modificar el stock del producto y guardarlo en la base de datos:
        producto.cantidad_en_stock = producto.cantidad_en_stock - cantidad_compra
        producto.save()
        
        return render(request, 'comprar_producto.html', {'producto': producto.nombre, 'cantidad_stock': producto.cantidad_en_stock})
    
    return render(request, 'comprar_producto.html')