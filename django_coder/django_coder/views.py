from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def pag_principal(request):
    return render(request, "index.html")