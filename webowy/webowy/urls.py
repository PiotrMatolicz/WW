"""
URL configuration for webowy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apka.views import *
import sklep.views as sv

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("hello", hello),
    path("czas", czas_txt),
    path("czas.html", czas_html),
    path("czas_szablon", czas_szablon),
    path("rozmowa", rozmowa),
    path("kalkulator_get", kalkulator_get),
    path("kalkulator_post", kalkulator_post),
    path("sklep/produkty.txt", sv.lista_towarow),
    path("sklep/produkty.html", sv.lista_towarow_html),
]
