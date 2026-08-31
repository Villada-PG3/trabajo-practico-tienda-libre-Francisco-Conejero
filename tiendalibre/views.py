from django.shortcuts import render


def home(request):
    contexto = {
        "titulo": "Ofertas de la semana",
        "usuario_logueado": True,
        "nombre_usuario": "Francisco",
        "productos_destacados": [
            {
                "nombre": "Auriculares Bluetooth",
                "precio": 15999,
                "stock": 32,
                "descripcion": "Auriculares inalámbricos con excelente calidad de sonido."
            },
            {
                "nombre": "Mouse inalámbrico",
                "precio": 8499,
                "stock": 18,
                "descripcion": "Mouse cómodo y práctico para uso diario."
            },
            {
                "nombre": "Teclado mecánico",
                "precio": 24999,
                "stock": 7,
                "descripcion": "Teclado mecánico ideal para estudiar y jugar."
            },
            {
                "nombre": "Webcam HD",
                "precio": 12999,
                "stock": 4,
                "descripcion": "Webcam HD para videollamadas."
            },
            {
                "nombre": "Pendrive 64GB",
                "precio": 5999,
                "stock": 1,
                "descripcion": "Pendrive de 64GB para guardar tus archivos."
            },
            {
                "nombre": "Hub USB-C",
                "precio": None,
                "stock": 0,
                "descripcion": "Hub USB-C con múltiples conexiones."
            },
        ],
    }

    return render(request, "tiendalibre/home.html", contexto)


def acerca_de_mi(request):
    return render(request, "tiendalibre/acerca-de-mi.html")