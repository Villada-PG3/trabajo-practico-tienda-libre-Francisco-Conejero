"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path
from tiendalibre import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("acerca-de-mi/", views.acerca_de_mi, name="acerca_de_mi"),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )