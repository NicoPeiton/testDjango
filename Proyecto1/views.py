from django import template
from django.http import HttpResponse
from datetime import datetime, date, timedelta
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola mundo!")

def segundaVista(request):
    return HttpResponse("<h1>Show me the money!</h1>")

def fecha(request):
    diaHoy = datetime.now()
    return HttpResponse(f"Fecha y hora actual:<br>{diaHoy}")

def apellido(request, ape):
    return HttpResponse(f"Mi apellido es: {ape}")

def cumpleanios(request):
    cumpleanios = datetime(2022, 6, 27, 18, 4)
    hoy = datetime.now()
    faltaCumple = cumpleanios - hoy
    return HttpResponse(f"Faltan: {faltaCumple} para tu cumple!")

def miEdad(request):
    nacimiento = datetime(1993, 6, 27, 18, 4)
    now = datetime.now()
    edad = now - nacimiento
    return HttpResponse(f"Hoy es: {now} Naciste el: {nacimiento} Tu edad es: {edad}")

def templateTest(request):

    mejorEstudiante = "Pepito"
    nota = 8.9

    dic1 = {"nombre":mejorEstudiante, "nota":nota}
    
    template = loader.get_template('template1.html')
    doc = template.render(dic1)
    return HttpResponse(doc)