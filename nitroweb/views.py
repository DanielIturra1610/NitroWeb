from django.shortcuts import render, redirect
from .models import Juego,Categoria
from django.contrib import messages


# Create your views here.

def index(request):
    context={}
    return render(request, 'nitroweb/index.html', context)

def nosotros(requets):
    context={}
    return render(request, 'nitroweb/Nosotros.html', context)

def games(request):
    context={}
    return render(request, 'nitroweb/games.html', context)

def iniciarsesion(request):
    context={}
    return render(request, 'nitroweb/IniciarSesion.html', context)

def classicgames(request):
    context={}
    return render(request, 'nitroweb/ClassicGames.html', context)

def contactanos(request):
    context={}
    return render(request, 'nitroweb/Contactanos.html', context)

def newgames(request):
    context={}
    return render(request, 'nitroweb/NewGames.html', context)

def newgames2(request):
    context={}
    return render(request, 'nitroweb/NewGames2.html', context)

def classicgames2(request):
    context={}
    return render(request, 'nitroweb/ClassicGames2.html', context)

def retrogames(request):
    context={}
    return render(request, 'nitroweb/RetroGames.html', context)

def retrogames2(request):
    context={}
    return render(request, 'nitroweb/RetroGames2.html', context)

def registrarse(request):
    context={}
    return render(request, 'nitroweb/Registrarse.html', context)

def satisf(request):
    context={}
    return render(request, 'nitroweb/Satisf.html', context)

def crud(request):
    juegos = Juego.objects.all()
    categorias = Categoria.objects.all()
    context={"juegos":juegos,"categorias":categorias}
    return render(request, 'main/crud.html', context)

def agregar(request):
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    categoria = request.POST['categoria']

    objCategoria = Categoria.objects.get(id = categoria)
    objJuego = Juego.objects.create(nombre=nombre, categoria=objCategoria, precio=precio)
    messages.success(request, 'Juego Agregado')
    return redirect('crud')

def eliminar(request, codigo):
    juego = Juego.objects.get(id=codigo)
    juego.delete()
    messages.success(request, 'Juego Eliminado')
    return redirect('crud')

def editar(request, codigo):
    juego = Juego.objects.get(id=codigo)
    categorias = Categoria.objects.all()
    context={"juego":juego,"categorias":categorias}
    return render(request, "main/editar.html", context)

def editarJuego(request):
    codigo = request.POST['id']
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    categoria = request.POST['categoria']

    objCategoria = Categoria.objects.get(id = categoria)
    objJuego = Juego.objects.get(id=codigo)
    
    objJuego.nombre = nombre
    objJuego.categoria = objCategoria
    objJuego.precio = precio
    objJuego.save()

    messages.success(request, 'Juego actualizado')
    return redirect('crud') 