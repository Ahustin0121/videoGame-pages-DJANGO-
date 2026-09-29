from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Videojuego
from .forms import VideojuegoForm


def videojuegos(request):
    productos = Videojuego.objects.all()
    return render(request, "videojuegos/videojuegos.html", {"productos": productos})


def detalle_videojuego(request, software_id):
    producto = get_object_or_404(Videojuego, pk=software_id)
    return render(request, "videojuegos/detalle.html", {"producto": producto})


@login_required
def gestionar_videojuegos(request):
    productos = Videojuego.objects.all()
    return render(request, "videojuegos/gestionar.html", {"productos": productos})


@login_required
def crear_videojuego(request):
    if request.method == "POST":
        form = VideojuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gestionar_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, "videojuegos/videojuego_form.html", {"form": form, "titulo": "Agregar Videojuego"})


@login_required
def editar_videojuego(request, pk):
    producto = get_object_or_404(Videojuego, pk=pk)
    if request.method == "POST":
        form = VideojuegoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('gestionar_videojuegos')
    else:
        form = VideojuegoForm(instance=producto)
    return render(request, "videojuegos/videojuego_form.html", {"form": form, "titulo": "Editar Videojuego", "producto": producto})


@login_required
def eliminar_videojuego(request, pk):
    producto = get_object_or_404(Videojuego, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('gestionar_videojuegos')
    return render(request, "videojuegos/eliminar.html", {"producto": producto})