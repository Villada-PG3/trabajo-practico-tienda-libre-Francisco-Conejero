from django.contrib import admin

# Register your models here.
from tiendalibre.models import Producto
from tiendalibre.models import Categoria

admin.site.register(Producto)
admin.site.register(Categoria)
