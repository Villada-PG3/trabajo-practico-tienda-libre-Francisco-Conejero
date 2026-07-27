from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]
    

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    marca = models.CharField(max_length=50, default="Marca Desconocida")

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos",
        null=True,
        blank=True #temporalmente se puede dejar en blanco, pero luego se puede hacer obligatorio
    )

    def __str__(self):
        return f"{self.nombre} - {self.precio} - {self.stock}"
