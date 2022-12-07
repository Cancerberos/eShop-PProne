from django.shortcuts import render
from eshopapp.models import Producto

# Create your views here.
def index(request):
        productos = Producto.objects.all().order_by("nombre")
        return render (request, "index.html", {"productos": productos})

def indexPopu(request): 
        productos = Producto.objects.all().filter(tipo__contains = 2).order_by("nombre")
        return render(request, "index.html", {"productos": productos})

def indexPromo(request): 
        productos = Producto.objects.all().filter(tipo__contains = 3).order_by("nombre")
        return render(request, "index.html", {"productos": productos})

def about(request): 
        #productos = Producto.objects.all().filter(tipo__contains = 3).order_by("nombre")
        return render(request, "about.html")