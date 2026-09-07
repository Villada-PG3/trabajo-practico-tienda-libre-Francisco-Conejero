# Consultas ORM — TiendaLibre

1. ```python
   Producto.objects.all()
   ```

2. ```python
   Producto.objects.values("nombre")
   ```

3. ```python
   Producto.objects.filter(precio__gt=1000)
   ```

4. ```python
   Producto.objects.filter(stock__gt=0)
   ```

5. ```python
   Producto.objects.filter(nombre__icontains="a")
   ```

6. ```python
   Producto.objects.filter(precio__lte=5000)
   ```

7. ```python
   Producto.objects.first()
   ```

8. ```python
   Producto.objects.order_by("precio")
   ```

9. ```python
   Producto.objects.filter(categoria__nombre="Yerbas")
   ```

10. ```python
    Producto.objects.all()[:3]
    ```
