from django.shortcuts import render
from django.http import HttpResponse

from Blog.models import Familiares
from Blog.models import Amigos
from Blog.models import Referidos
from django.core import serializers

from Blog.forms import FamiliaresFormulario
from Blog.forms import AmigosFormulario
from Blog.forms import ReferidosFormulario

# Create your views here.
def inicio(request):
    return render(request,"Blog/inicio.html")

def buscar(request):
    apellido_views = request.GET['apellido']
    familiares_todos = Familiares.objects.filter(apellido=apellido_views)
    return render(request,"Blog/resultadoFamiliares.html", {"apellido":apellido_views,"apellido":familiares_todos})

def buscarfamiliar(request):
    return render(request,"Blog/busquedaFamiliares.html")

def otrabusqueda(request):
    apellido_views = request.GET['apellido']
    amigos_todos = Amigos.objects.filter(apellido=apellido_views)
    return render(request,"Blog/resultadoAmigos.html", {"apellido":apellido_views,"apellido":amigos_todos})

def buscaramigo(request):
    return render(request,"Blog/busquedaAmigos.html")

def otrabusqueda_2(request):
    apellido_views = request.GET['apellido']
    referidos_todos = Referidos.objects.filter(apellido=apellido_views)
    return render(request,"Blog/resultadoReferidos.html", {"apellido":apellido_views,"apellido":referidos_todos})

def buscarreferido(request):
    return render(request,"Blog/busquedaReferidos.html")






def familiares(request):
    if request.method == "POST":
            miFormulario = FamiliaresFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  familiares = Familiares(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], dni=informacion["dni"])
                  familiares.save()
                  return render(request, "Blog/inicio.html")
    else:
        miFormulario = FamiliaresFormulario()
 
    return render(request, "Blog/familiares.html", {"miFormulario": miFormulario})

def familiaresapi(request):
    familiares_todos = Familiares.objects.all()
    return HttpResponse(serializers.serialize('json',familiares_todos))

def amigos(request):
    if request.method == "POST":
            miFormulario = AmigosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  amigos = Amigos(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], dni=informacion["dni"])
                  amigos.save()
                  return render(request, "Blog/inicio.html")
    else:
        miFormulario = AmigosFormulario()
 
    return render(request, "Blog/amigos.html", {"miFormulario": miFormulario})



def amigosapi(request):
    amigos_todos = Amigos.objects.all()
    return HttpResponse(serializers.serialize('json',amigos_todos))




def referidos(request):
    if request.method == "POST":
            miFormulario = ReferidosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  referidos = Referidos(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], dni=informacion["dni"])
                  referidos.save()
                  return render(request, "Blog/inicio.html")
    else:
        miFormulario = ReferidosFormulario()
 
    return render(request, "Blog/referidos.html", {"miFormulario": miFormulario})

def referidosapi(request):
    referidos_todos = Referidos.objects.all()
    return HttpResponse(serializers.serialize('json',referidos_todos))



# def amigos(request):
#    return HttpResponse("vista")
#def amigos(request):
#   return render (request,"Blog/amigos.html")

from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class FamiliaresList(ListView):
    model = Familiares
    template = 'Blog/familiares_list.html'

class FamiliaresCreate(CreateView):
    model = Familiares
    fields = '__all__'
    success_url = '/Blog/familiares/list/'

class FamiliaresEdit(UpdateView):
    model = Familiares
    fields = '__all__'
    success_url = '/Blog/familiares/list/'

from django.views.generic.detail import DetailView

class FamiliaresDetail(DetailView):
    model = Familiares
    template = 'Blog/familiares_detail.html'

class FamiliaresDelete(DeleteView):
    model = Familiares
    success_url = '/Blog/familiares/list/'

class AmigosList(ListView):
    model = Amigos
    template = 'Blog/amigos_list.html'

class AmigosCreate(CreateView):
    model = Amigos
    fields = '__all__'
    success_url = '/Blog/amigos/list/'

class AmigosEdit(UpdateView):
    model = Amigos
    fields = '__all__'
    success_url = '/Blog/amigos/list/'

class AmigosDetail(DetailView):
    model = Amigos
    template = 'Blog/amigos_detail.html'

class AmigosDelete(DeleteView):
    model = Amigos
    success_url = '/Blog/amigos/list/'


class ReferidosList(ListView):
    model = Referidos
    template = 'Blog/referidos_list.html'

class ReferidosCreate(CreateView):
    model = Referidos
    fields = '__all__'
    success_url = '/Blog/referidos/list/'

class ReferidosEdit(UpdateView):
    model = Referidos
    fields = '__all__'
    success_url = '/Blog/referidos/list/'

class ReferidosDetail(DetailView):
    model = Referidos
    template = 'Blog/referidos_detail.html'

class ReferidosDelete(DeleteView):
    model = Referidos
    success_url = '/Blog/referidos/list/'



    