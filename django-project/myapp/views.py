from django.urls import reverse
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse

from . import forms
from .models import Curso

import requests
import sqlite3


def index (request):
    #f = open("myapp/index.html", encoding="utf-8")
    #response = HttpResponse(f.read())
    #f.close()
    context = {"nombre":"Facundo", "descripcion":"programador Python", "cursos": {"mayo":"MySQL", "junio":"Django"}, "tecnologias": ["JavaScript","Python","MySQL","Angular_"], "librosLeidos": 20, "libros":["Salomé","El príncipe","El resplandor"],"sinValor":""}
    return render(request, "myapp/index.html", context)

def curso (request, nombre_curso):
    miConexion = sqlite3.connect('db.sqlite3')
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT CURSO, INTEGRANTES FROM CURSOS WHERE CURSO=?", [nombre_curso])
    contenido = miCursor.fetchone()
    miConexion.close()
    #context = {"curso": contenido}
    if contenido is None:
        raise Http404

    nombre, inscriptos = contenido
    context = {"nombre":nombre, "inscriptos":inscriptos}
    return render(request, "myapp/curso.html", context)

def cursos(request):
    miConexion = sqlite3.connect('db.sqlite3')
    miCursor = miConexion.cursor()
    #miCursor.execute("SELECT CURSO, INTEGRANTES FROM CURSOS WHERE CURSO LIKE 'J%' ")
    miCursor.execute("SELECT CURSO, INTEGRANTES FROM CURSOS")
    contenido = miCursor.fetchall()
    context = {"cursos": contenido}
    miConexion.close()
    return render(request, "myapp/cursos.html", context)

def curso_API (request):
    miConexion = sqlite3.connect('db.sqlite3')
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT CURSO, INTEGRANTES FROM CURSOS")
    response = JsonResponse(miCursor.fetchall(), safe=False)
    #response = JsonResponse(dict(miCursor.fetchall()))
    miConexion.close()
    context = {"respuesta":response}
    return render(request, "myapp/curso_API.html", context)

def nuevo_curso (request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            miConexion = sqlite3.connect('db.sqlite3')
            miCursor = miConexion.cursor()
            miCursor.execute("INSERT INTO CURSOS VALUES (?,?)", 
                            (form.cleaned_data['nombre'], form.cleaned_data['inscriptos'])
                            )
            miConexion.commit()
            miConexion.close()
            return HttpResponseRedirect(reverse("listaCursos"))
    else:
        form = forms.FormularioCurso()

    context = {"formulario":form}
    return render(request, "myapp/nuevo_curso.html", context)

def cursoORM(request, nombre_curso):
    try:
        curso = Curso.objects.get(nombre=nombre_curso) 
    except Curso.DoesNotExist:
        raise Http404
    
    context = {"curso":curso}
    return render(request, "myapp/cursoORM.html", context)

def cursosORM (request):
    cursos = Curso.objects.all().order_by('nombre')
    context = {"cursos":cursos}
    return render(request, "myapp/cursosORM.html", context)

def cursos_API_ORM (request):
    response = JsonResponse(list(Curso.objects.values()), safe=False)
    return response

def nuevoCursoORM(request):
    if request.method == "POST":
        form = forms.FormularioCursoORM(request.POST)
        if form.is_valid():
            Curso.objects.create(nombre=form.cleaned_data['nombre'], inscriptos = form.cleaned_data['inscriptos'])
            return HttpResponseRedirect(reverse("listaCursosORM"))
    else:
        form = forms.FormularioCursoORM()

    context = {"formulario":form}
    return render(request, "myapp/nuevo_cursoORM.html", context)

def index1 (request):
    return HttpResponse("<h1>Hola, mundo!</h1>")

def cursos1 (request):
    miConexion = sqlite3.connect('db.sqlite3')
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT CURSO, INTEGRANTES FROM CURSOS")

    html = """
    <html> 
    <title> Lista de cursos </title>
    <table style ="border: 1px solid">
    <thead> <tr>
    <th>Curso</th> <th>Inscriptos</th>
    </tr></thead> 
    """

    for (categoria, integrantes) in miCursor.fetchall():
        html += f"""
            <tr>
            <td> {categoria} </td>
            <td> {integrantes} </td>
            </tr>
        """
    
    html += "</table> </html>"
    miConexion.close()
    return HttpResponse(html)

def dolar (request):
    r = requests.get("https://api.recursospython.com/dollar")
    precio = r.json()

    html = f"""
    <p> Precio {precio["buy_price"]} </p>
    <p> Precio {precio["sale_price"]} </p>
    """

    return HttpResponse(html)

def aeropuertos (request):

    f = open("aeropuertos.csv", encoding="utf8")

    html = """
    <html> <title> Aeropuertos </title>
    <table style ="border: 1px solid">
    <thead> <tr>
    <th>Aeropuerto</th> <th>Ciudad</th> <th>País</th>
    </tr></thead> 
    """

    for linea in f:
        datos = linea.split(",")
        nombre = datos[1].replace('"', "")
        ciudad = datos[2].replace('"', "")
        pais = datos[3].replace('"', "")
        html += f"""
            <tr>
              <td>{nombre}</td>
              <td>{ciudad}</td>
              <td>{pais}</td>
            </tr>
        """
    f.close()
    
    html += "</table> </html>"

    return HttpResponse(html)

def aeropuertos_json (request):
    f = open("aeropuertos.csv", encoding="utf8")
    aeropuertos = []
    for linea in f:
        datos = linea.split(",")
        aeropuerto = {
            "Nombre": datos[1].replace('"', ""),
            "Ciudad": datos[2].replace('"', ""),
            "Pais": datos[3].replace('"', "")
        } 
        aeropuertos.append(aeropuerto)

    f.close()
    
    return JsonResponse(aeropuertos, safe=False)

def aeropuerto_template (request):
    f = open("aeropuertos.csv", encoding="utf8")
    lista_aeropuertos = []
    for linea in f:
        datos = linea.split(",")
        nombre = datos[1].replace('"', "")
        ciudad = datos[2].replace('"', "")
        pais = datos[3].replace('"', "")
        lista_aeropuertos.append((nombre, ciudad, pais))
    f.close()
    context = {"lista": lista_aeropuertos}
    return render(request, "tareas/aeropuertos.html", context)

def nueva_pelicula (request):
    if request.method == "POST":
        form = forms.FormularioPeliculas(request.POST)
        if form.is_valid():
            conexion = sqlite3.connect("db.sqlite3")
            miCursor = conexion.cursor()
            miCursor.execute("INSERT INTO peliculas VALUES (?,?,?,?)", 
                            (form.cleaned_data["nombre"],form.cleaned_data["fechaDeEstreno"],form.cleaned_data["mayoresDe"],form.cleaned_data["preventa"],)
                            )
            miCursor.execute("SELECT Nombre,FechaDeEstreno,MayoresDe,PreventaOnline FROM peliculas")
            peliculas = miCursor.fetchall()   
            conexion.commit()
            conexion.close()
            context = {"formulario":form, "peliculas": peliculas, "reciente":form.cleaned_data}
            return render(request, "tareas/listaPeliculas.html", context)

    else:
        form = forms.FormularioPeliculas()

    
    context = {"formulario":form}
    return render (request, "tareas/nueva_pelicula.html", context)