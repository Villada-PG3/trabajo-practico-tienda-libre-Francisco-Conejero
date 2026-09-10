# Consultas ORM — TiendaLibre

1. ```
   Producto.objects.all()
   ```

2. ```
   Producto.objects.values("nombre")
   ```

3. ```
   Producto.objects.filter(precio__gt=1000)
   ```

4. ```
   Producto.objects.filter(stock__gt=0)
   ```

5. ```
   Producto.objects.filter(nombre__icontains="a")
   ```

6. ```
   Producto.objects.filter(precio__lte=5000)
   ```

7. ```
   Producto.objects.first()
   ```

8. ```
   Producto.objects.order_by("precio")
   ```

9. ```
   Producto.objects.filter(categoria__nombre="Yerbas")
   ```

10. ```
    Producto.objects.all()[:3]
    ```
