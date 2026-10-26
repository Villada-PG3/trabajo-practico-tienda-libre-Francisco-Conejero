
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
    paginate_by = 6

    def get_queryset(self):
        return Producto.objects.filter(
            activo=True
        ).order_by("fecha_creacion")


class DetalleProductoView(DetailView):
    model = Producto
    template_name = "tiendalibre/detalle.html"
    context_object_name = "producto"

    def get_queryset(self):
        return Producto.objects.filter(activo=True)


class AcercaDeMiView(TemplateView):
    template_name = "tiendalibre/acerca-de-mi.html"
