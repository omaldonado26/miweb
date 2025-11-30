from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1 style='text-align:center; margin-top:50px;'>Hola Mundo desde Django 🎉</h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
