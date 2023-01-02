from django.http import HttpResponse
from django.template import Template, Context
import os.path

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATES_PATH = os.path.join(PROJECT_PATH, 'templates/')

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def probandoTemplate(self):
    nom = "Martin"
    ape = "Lopez"

    diccionario = {
        "nombre":nom,
        "apellido":ape,
        "notas": [10,7,8,10,9],
    }

    miHtml = open(TEMPLATES_PATH+"/template1.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)