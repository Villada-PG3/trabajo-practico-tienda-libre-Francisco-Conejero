from django.shortcuts import render

from tiendalibre.models import Producto


def home(request):
    productos = Producto.objects.filter(activo=True).order_by('-fecha_creacion')[:3]

    contexto = {
        "productos": productos
    }

    return render(request, "tiendalibre/home.html", contexto)


def catalogo(request):
    productos = Producto.objects.filter(activo=True).order_by('fecha_creacion')
    contexto = {"productos": productos }
    return render(request, "tiendalibre/catalogo.html", contexto)


def acerca_de_mi(request):
    return render(request, "tiendalibre/acerca-de-mi.html")