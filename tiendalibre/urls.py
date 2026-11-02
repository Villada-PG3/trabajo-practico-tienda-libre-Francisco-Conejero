
from django.urls import path
from . import views

app_name = "tiendalibre"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("acerca-de-mi/", views.AcercaDeMiView.as_view(), name="acerca_de_mi"),
    path("catalogo/", views.CatalogoView.as_view(), name="catalogo"),
    path("categoria/<slug:slug>/", views.CategoriaView.as_view(), name="categoria"),

    path(
        "producto/nuevo/",
        views.ProductoCreateView.as_view(),
        name="producto_nuevo"
    ),

    path(
        "producto/<int:pk>/editar/",
        views.ProductoUpdateView.as_view(),
        name="producto_editar"
    ),

    path(
        "producto/<int:pk>/",
        views.DetalleProductoView.as_view(),
        name="detalle_producto"
    ),

    path("contacto/", views.contacto, name="contacto"),
]
