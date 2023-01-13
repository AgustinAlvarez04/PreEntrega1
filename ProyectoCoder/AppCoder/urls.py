from django.urls import path
from .views import *


urlpatterns= [
    path('curso/', curso),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores" ),
    path('entregables/', entregables, name="Entregables"),
    path("", inicio, name="Inicio"),
]