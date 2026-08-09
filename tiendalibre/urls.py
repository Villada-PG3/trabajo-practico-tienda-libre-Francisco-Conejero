from django.shortcuts import render
from .models import Producto


def home(request):
    return render(request, "tiendalibre/home.html")


def acerca_de_mi(request):
    return render(request, "tiendalibre/acerca-de-mi.html")


def productos(request):
    lista_productos = Producto.objects.all()

    contexto = {
        "productos": lista_productos
    }

    return render(request, "productos.html", contexto)