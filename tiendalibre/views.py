
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_object_or_404, render
from tiendalibre.models import Producto, Categoria
from .forms import ContactoForm


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
        queryset = Producto.objects.filter(activo=True)

        busqueda = self.request.GET.get("q", "").strip()

        if busqueda:
            queryset = queryset.filter(
                Q(nombre__icontains=busqueda)
                | Q(marca__icontains=busqueda)
                | Q(descripcion__icontains=busqueda)
            )

        return queryset.order_by("fecha_creacion")


class CategoriaView(ListView):
    model = Producto
    template_name = "tiendalibre/categoria.html"
    context_object_name = "productos"
    paginate_by = 6

    def get_queryset(self):
        self.categoria = get_object_or_404(
            Categoria,
            slug=self.kwargs["slug"]
        )

        return Producto.objects.filter(
            categoria=self.categoria,
            activo=True
        ).order_by("nombre")

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["categoria"] = self.categoria
        return contexto


class DetalleProductoView(DetailView):
    model = Producto
    template_name = "tiendalibre/detalle.html"
    context_object_name = "producto"

    def get_queryset(self):
        return Producto.objects.filter(activo=True)


class AcercaDeMiView(TemplateView):
    template_name = "tiendalibre/acerca-de-mi.html"


def contacto(request):
    enviado = False

    if request.method == "POST":
        form = ContactoForm(request.POST)

        if form.is_valid():
            enviado = True
            form = ContactoForm()
    else:
        form = ContactoForm()

    return render(
        request,
        "tiendalibre/contacto.html",
        {
            "form": form,
            "enviado": enviado,
        }
    )
