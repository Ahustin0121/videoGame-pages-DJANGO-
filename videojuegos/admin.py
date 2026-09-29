from django.contrib import admin
from .models import Videojuego


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "consola", "precio", "stock", "Estado")
    list_filter = ("Estado", "consola")
    search_fields = ("nombre", "descripcion")
    list_editable = ("precio", "stock")