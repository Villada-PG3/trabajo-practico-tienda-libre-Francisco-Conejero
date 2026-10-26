from django.urls import path
from . import views

app_name = "tiendalibre"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "acerca-de-mi/",
        views.AcercaDeMiView.as_view(),
        name="acerca_de_mi",
    ),
    path("catalogo/", views.CatalogoView.as_view(), name="catalogo"),
    path(
        "producto/<int:pk>/",
        views.DetalleProductoView.as_view(),
        name="detalle_producto",
    ),
]
