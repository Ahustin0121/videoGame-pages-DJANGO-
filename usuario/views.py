from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from videojuegos.models import Videojuego


def inicio(request):
    videojuego_destacado = Videojuego.objects.filter(nombre__icontains="Zelda").first()
    return render(request, "index.html", {"videojuego_destacado": videojuego_destacado})


def contacto(request):
    return render(request, "usuario/contacto.html")


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            proxima = request.GET.get("next")
            if proxima:
                return redirect(proxima)
            return redirect("gestionar_videojuegos")
        return render(
            request,
            "usuario/admin_login.html",
            {"error": "Usuario o contraseña incorrectos."},
        )
    if request.user.is_authenticated:
        return redirect("gestionar_videojuegos")
    aviso = bool(request.GET.get("next"))
    return render(request, "usuario/admin_login.html", {"aviso": aviso})


def admin_logout(request):
    logout(request)
    return redirect("admin_login")