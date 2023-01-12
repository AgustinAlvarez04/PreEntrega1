from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

def curso(request):
    cursito= Curso(nombre="python", comision=123456)
    cursito.save()
    cadena_texto=f"Curso guardado: Nombre:{cursito.nombre}, Comision:{cursito.comision}"
    return HttpResponse(cadena_texto)