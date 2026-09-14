from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
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

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    return render(
        request,
        "tiendalibre/detalle.html",
        {"producto": producto}
    )


def acerca_de_mi(request):
    return render(request, "tiendalibre/acerca-de-mi.html")