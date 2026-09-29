import shutil
from pathlib import Path

from django.conf import settings
from django.db import migrations


def copiar_a_media(apps, schema_editor):
    Videojuego = apps.get_model("videojuegos", "Videojuego")
    origen_base = Path(settings.BASE_DIR) / "static"
    destino_base = Path(settings.MEDIA_ROOT)
    for videojuego in Videojuego.objects.all():
        campo = videojuego.imagen
        ruta = getattr(campo, "name", campo)
        if not ruta:
            continue
        origen = origen_base / ruta
        destino = destino_base / ruta
        if origen.exists() and not destino.exists():
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(origen, destino)


def revertir(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("videojuegos", "0003_alter_videojuego_imagen"),
    ]

    operations = [
        migrations.RunPython(copiar_a_media, revertir),
    ]