from django.http import HttpResponse
from django.template import loader

def saludo(request):
	return HttpResponse("Hola Comisión 56050")

def ver_comision(request):
    nro_comision = 56050
    
    diccionario = {"numero_comision": nro_comision}
    
    template = loader.get_template("template.html")
    
    doc = template.render(diccionario)
    
    return HttpResponse(doc)