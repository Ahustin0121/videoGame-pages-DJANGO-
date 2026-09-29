from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from usuario.views import inicio, contacto, admin_login, admin_logout
from consolas.views import consolas, detalle_consola
from videojuegos.views import videojuegos, detalle_videojuego, gestionar_videojuegos, crear_videojuego, editar_videojuego, eliminar_videojuego

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio),
    path('adminlogin/', admin_login, name='admin_login'),
    path('adminlogout/', admin_logout, name='admin_logout'),
    path('consola/',consolas, name='consolas'),
    path('consolas/<str:hardware_id>/', detalle_consola, name='detalle_consola'),
    path('videojuegos/',videojuegos, name='videojuegos'),
    path('videojuegos/gestionar/', gestionar_videojuegos, name='gestionar_videojuegos'),
    path('videojuegos/nuevo/', crear_videojuego, name='crear_videojuego'),
    path('videojuegos/editar/<int:pk>/', editar_videojuego, name='editar_videojuego'),
    path('videojuegos/eliminar/<int:pk>/', eliminar_videojuego, name='eliminar_videojuego'),
    path('videojuegos/<int:software_id>/', detalle_videojuego, name='detalle_videojuego'),
    path('contacto/',contacto, name='contacto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
