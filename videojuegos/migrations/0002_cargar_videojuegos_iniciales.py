from django.db import migrations


VIDEOJUEGOS = [
    {
        "nombre": "Red Dead Redemption 2",
        "stock": 20,
        "consola": "PlayStation 4",
        "Estado": "Nuevo",
        "ano": 2018,
        "PEGI": "+18",
        "descripcion": "Juego de acción y aventura en un vasto mundo abierto desarrollado por Rockstar Games.",
        "precio": "29.000",
        "imagen": "images/videojuegos/red.png",
    },
    {
        "nombre": "Cyberpunk 2077",
        "stock": 21,
        "consola": "PlayStation 5",
        "Estado": "Nuevo",
        "ano": 2022,
        "PEGI": "+18",
        "descripcion": "Un juego de rol de acción y mundo abierto ambientado en la futurista y peligrosa megalópolis de Night City",
        "precio": "39.000",
        "imagen": "images/videojuegos/cyber.png",
    },
    {
        "nombre": "The Legend Of Zelda Tears Of The Kingdom",
        "stock": 20,
        "consola": "switch/switch 2",
        "Estado": "Nuevo",
        "ano": 2023,
        "PEGI": "+10",
        "descripcion": "Videojuego de acción y aventura en mundo abierto desarrollado por Nintendo, Link y la Princesa Zelda investigan un misterio bajo el Castillo de Hyrule",
        "precio": "59.000",
        "imagen": "images/videojuegos/tloz.jpeg",
    },
    {
        "nombre": "Guitar Hero 2",
        "stock": 10,
        "consola": "PlayStation 2",
        "Estado": "Como Nuevo",
        "ano": 2006,
        "PEGI": "+12",
        "descripcion": "Videojuego de ritmo musical desarrollado por Harmonix, usas el mando para pulsar los trastes de colores al ritmo del ROCK",
        "precio": "19.000",
        "imagen": "images/videojuegos/gh2.png",
    },
    {
        "nombre": "Guitar Hero 3",
        "stock": 10,
        "consola": "xbox 360",
        "Estado": "Como Nuevo",
        "ano": 2007,
        "PEGI": "+12",
        "descripcion": "Juego de ritmo y música lanzado en octubre de 2007, desarrollado por Neversoft y publicado por Activision. Luego de sus 2 juegos anteriores guitar hero 2 y guitar hero 1",
        "precio": "19.000",
        "imagen": "images/videojuegos/gh3.png",
    },
    {
        "nombre": "Silent Hills 3",
        "stock": 20,
        "consola": "PlayStation 2",
        "Estado": "Como Nuevo",
        "ano": 2003,
        "PEGI": "+18",
        "descripcion": "Videojuego de terror psicológico y supervivencia. La protagonista es Heather Mason, una adolescente común que lleva una vida tranquila. De repente, Heather queda atrapada en una pesadilla llena de monstruos y realidades alternativas.",
        "precio": "79.000",
        "imagen": "images/videojuegos/sh3.png",
    },
    {
        "nombre": "Sonic hedgehog",
        "stock": 4,
        "consola": "SEGA GENESIS",
        "Estado": "Poco Usado",
        "ano": 1991,
        "PEGI": "+6",
        "descripcion": "Un clásico videojuego de plataformas desarrollado por Sega. Sonic, un erizo azul que corre a velocidades supersónicas.",
        "precio": "89.000",
        "imagen": "images/videojuegos/sonic.jpeg",
    },
]


def cargar_datos(apps, schema_editor):
    Videojuego = apps.get_model("videojuegos", "Videojuego")
    for datos in VIDEOJUEGOS:
        Videojuego.objects.get_or_create(nombre=datos["nombre"], defaults=datos)


def eliminar_datos(apps, schema_editor):
    Videojuego = apps.get_model("videojuegos", "Videojuego")
    Videojuego.objects.filter(nombre__in=[d["nombre"] for d in VIDEOJUEGOS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("videojuegos", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(cargar_datos, eliminar_datos),
    ]