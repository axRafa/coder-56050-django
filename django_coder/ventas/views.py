from django.shortcuts import render, redirect
from ventas.forms import ClienteFormulario
from ventas.models import Cliente, Venta
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

##################### CRUD CLIENTES ############################

def crear_cliente(request):
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente(
                nombre=informacion["nombre"],
                nro_cuit=informacion["nro_cuit"],
                email=informacion["email"]
                )
            cliente.save()
            return render(request, "index.html")
        else:
            return render(request, 'ventas/crear_cliente.html', {"errors": mi_formulario.errors})
    else:
        mi_formulario = ClienteFormulario()
        return render(request, "ventas/crear_cliente.html", {"mi_formulario": mi_formulario})
    
def leer_clientes(request):
    lista_clientes = Cliente.objects.all()
    return render(request, "ventas/leer_clientes.html", {"clientes": lista_clientes})

def eliminar_cliente(request, nombre_cliente):
    cliente = Cliente.objects.get(nombre=nombre_cliente)
    cliente.delete()
    return redirect('leer clientes')

def editar_cliente(request, nombre_cliente):
    cliente = Cliente.objects.get(nombre=nombre_cliente)
    
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente.nombre = informacion['nombre']
            cliente.nro_cuit = informacion['nro_cuit']
            cliente.email = informacion['email']
            cliente.save()
            return render(request, "index.html")
    else:
        mi_formulario = ClienteFormulario()
        return render(request, "ventas/editar_cliente.html", {"mi_formulario": mi_formulario})
    
###################### CRUD VENTAS #############################

class VentaListView(ListView):
    model = Venta
    context_object_name = "ventas"
    template_name = "ventas/ventas_lista.html"

class VentaCreateView(CreateView):
    model = Venta
    template_name = "ventas/ventas_crear.html"
    success_url = reverse_lazy('ventas lista')
    fields = ['cliente', 'nro_transaccion', 'producto', 'cantidad', 'fecha_de_venta']

class VentaUpdateView(UpdateView):
    pass

class VentaDeleteView(DeleteView):
    pass
