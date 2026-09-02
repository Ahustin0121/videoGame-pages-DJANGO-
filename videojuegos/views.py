from django.shortcuts import render

# Dejamos solo los datos de videojuegos
data = {
    "red2": {
        "nombre": "Red Dead Redemption 2",
        "stock": 20,
        "consola": "PlayStation 4",
        "Estado": "Nuevo",
        "ano": 2018,
        "PEGI": "+18",
        "descripcion": "Juego de acción y aventura en un vasto mundo abierto desarrollado por Rockstar Games.",
        "precio": "29.000",
        "imagen": "images/videojuegos/red.png"
    },
    "cyberpunk": {
            "nombre": "Cyberpunk 2077",
            "stock": 21,
            "consola": "PlayStation 5",
            "Estado": "Nuevo",
            "ano": 2022,
            "PEGI": "+18", 
            "descripcion": "un juego de rol de acción y mundo abierto ambientado en la futurista y peligrosa megalópolis de Night City",
            "precio": "39.000",
            "imagen": "images/videojuegos/cyber.png"
        },
    "tloz": {
            "nombre": "The Legend Of Zelda Tears Of The Kingdom",
            "stock": 20,
            "consola": "switch/switch 2",
            "Estado": "Nuevo",
            "ano": 2023,
            "PEGI": "+10",
            "descripcion": "videojuego de acción y aventura en mundo abierto desarrollado por Nintendo, Link y la Princesa Zelda investigan un misterio bajo el Castillo de Hyrule",
            "precio": "59.000",
            "imagen": "images/videojuegos/tloz.jpeg"
        },
    "guitar-hero2": {
            "nombre": "Guitar Hero 2",
            "stock": 10,
            "consola": "PlayStation 2",
            "Estado": "Como Nuevo",
            "ano": 2006,
            "PEGI": "+12", 
            "descripcion": "videojuego de ritmo musical desarrollado por Harmonix, usas el mando para pultar los trastes de colores al ritmo del ROCK",
            "precio": "19.000",
            "imagen": "images/videojuegos/gh2.png"
        },
    "guitar-hero3": {
            "nombre": "Guitar Hero 3",
            "stock": 10,
            "consola": "xbox 360",
            "Estado": "Como Nuevo",
            "ano": 2007,
            "PEGI": "+12",
            "descripcion": "Juego de ritmo y música lanzado en octubre de 2007, desarrollado por Neversoft y publicado por Activision. luego de sus 2 juegos anteriores guitar hero 2 y guitar hero 1",
            "precio": "19.000",
            "imagen": "images/videojuegos/gh3.png"
        },
    "sh3": {
            "nombre": "Silent Hills 3",
            "stock": 20,
            "consola": "PlayStation 2",
            "Estado": "Como Nuevo",
            "ano": 2003,
            "PEGI": "+18", 
            "descripcion": "videojuego de terror psicológico y supervivencia,La protagonista es Heather Mason, una adolescente común que lleva una vida tranquila,De repente, Heather queda atrapada en una pesadilla llena de monstruos y realidades alternativas.",
            "precio": "79.000",
            "imagen": "images/videojuegos/sh3.png"
        },
    "sonic": {
            "nombre": "Sonic hedgehog",
            "stock": 4,
            "consola": "SEGA GENESIS",
            "Estado": "Poco Usado",
            "ano": 1991,
            "PEGI": "+6",
            "descripcion": "un clásico videojuego de plataformas desarrollado por Sega, Sonic, un erizo azul que corre a velocidades supersónicas.",
            "precio": "89.000",
            "imagen": "images/videojuegos/sonic.jpeg"
        }                      
}

def videojuegos(request):
    return render(request, "videojuegos/videojuegos.html", {"productos": data})

def detalle_videojuego(request, software_id):
    producto_seleccionado = data.get(software_id)
    # Apuntamos a la carpeta correcta de videojuegos
    return render(request, "videojuegos/detalle.html", {"producto": producto_seleccionado})