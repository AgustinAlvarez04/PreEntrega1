from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

def curso(request):
    cursito= Curso(nombre="python", comision=123456)
    cursito.save()
    cadena_texto=f"Curso guardado: Nombre:{cursito.nombre}, Comision:{cursito.comision}"
    return HttpResponse(cadena_texto)

def cursos(request):
    return HttpResponse("esto es una vista de cursos")

def estudiantes(request):
    return HttpResponse("Esto es una vista de estudiantes")

def profesores(request):
    return HttpResponse("Esto es una vista de profesores")

def entregables(request):
    return HttpResponse("Esto es una vista de entregables")

def inicio(request):
    return HttpResponse("Esto es el inicio")
