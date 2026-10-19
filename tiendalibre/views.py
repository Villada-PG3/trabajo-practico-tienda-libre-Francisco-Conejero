
from django.views.generic import TemplateView, ListView, DetailView
from tiendalibre.models import Producto


class HomeView(TemplateView):
    template_name = "tiendalibre/home.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto["productos"] = Producto.objects.filter(
            activo=True
        ).order_by("-fecha_creacion")[:3]

        return contexto


class CatalogoView(ListView):
    model = Producto
    template_name = "tiendalibre/catalogo.html"
    context_object_name = "productos"

    def get_queryset(self):
        return Producto.objects.filter(
            activo=True
        ).order_by("fecha_creacion")


def detalle_producto(request, pk):
    from django.shortcuts import get_object_or_404, render

    producto = get_object_or_404(Producto, pk=pk)

    return render(
        request,
        "tiendalibre/detalle.html",
        {"producto": producto}
    )


def acerca_de_mi(request):
    return TemplateView.as_view(
        template_name="tiendalibre/acerca-de-mi.html"
    )(request)
