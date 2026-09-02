from django.contrib import admin
from django.urls import path
from usuario.views import inicio
from consolas.views import consolas, detalle_consola
from videojuegos.views import videojuegos, detalle_videojuego
from usuario.views import contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio),
    path('consola/',consolas, name='consolas'),
    path('consolas/<str:hardware_id>/', detalle_consola, name='detalle_consola'),
    path('videojuegos/',videojuegos, name='videojuegos'),
    path('videojuegos/<str:software_id>/', detalle_videojuego, name='detalle_videojuego'),
    path('contacto/',contacto, name='contacto'),
]
