from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Produkt

# Create your views here.
def lista_towarow(request:HttpRequest) -> HttpResponse:
    produkty = Produkt.objects.all()
    return HttpResponse(str(produkty), content_type='text/plain')


def lista_towarow_html(request:HttpRequest) -> HttpResponse:
    produkty = Produkt.objects.all()

    # Produkty to są normalne obiekty Pythona
    # for p in produkty:
    #     print(p.cena)

    return render(request=request,
                  template_name='towary.html',
                  context={'towary': produkty})