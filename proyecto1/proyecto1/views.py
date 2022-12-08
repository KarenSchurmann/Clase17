from django.http import HttpResponse    
import datetime
from django.template import Template, Context, loader
def saludo(request):
        return HttpResponse ("Hola mundo")

def segunda_vista(request):
    return HttpResponse("Bien, ya vamos entendiendo esto de las views")

def dia_de_hoy(request):
    diadehoy=datetime.datetime.now()
    cadena=f"Hoy es {diadehoy}"
    return HttpResponse (cadena)

def saludar_con_nombre(request,nombre):
    saludo=f"Hola {nombre}"
    return HttpResponse (saludo)

def probando_html(request):
    nom="Kai"   
    ap="Schurmann"

    diccionario={"nombre":nom,"apellido":ap, "edad": 26, "lista": [1,2,3,4,5,6]}

    #archivo=open("./templates/template1.html")
    #template=Template(archivo.read())
    #archivo.close()

    #documento=template.render(contexto)


    #Todo esto cambia por:

    plantilla=loader.get_template('template1.html')

    #contexto=Context(diccionario) ya no es necesario utilizar esta linea, ya que renderizo la plantilla que ya tiene el diccionario.

    documento=plantilla.render(diccionario)
    return HttpResponse (documento)

def probando_segundo_html(request):

    diccionario={"Estudiantes": ["Facu","Leo","Kai","Marcos"] , "Comision": 1234}

    plantilla= loader.get_template('coderhouse.html')

    documento= plantilla.render(diccionario)
    return HttpResponse(documento)