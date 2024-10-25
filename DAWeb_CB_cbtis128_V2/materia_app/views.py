from django.shortcuts import render
from .models import Materia

# Create your views here.

def inicio_vista(request):
    # obtener todos los registros de la tabla materia
    ListadoMaterias=Materia.objects.all()
    return render(request,"gestionarMateria.html",{"lasmaterias":ListadoMaterias})
