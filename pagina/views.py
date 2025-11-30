from django.shortcuts import render


def inicio(request):
    return render(request, "pagina/inicio.html")


def servicios(request):
    return render(request, "pagina/servicios.html")


def contacto(request):
    return render(request, "pagina/contacto.html")
