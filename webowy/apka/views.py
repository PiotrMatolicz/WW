from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
# Tutaj definiujemy funkcje, które zostaną wywołane, gdy na serwer przyjdą określone zapytania

def hello(request):
    return HttpResponse('Hello <b style="color:red">world</b>')


def czas_txt(request):
    return HttpResponse(str(datetime.now()))


def czas_html(request:HttpRequest) -> HttpResponse:
    godzina = datetime.now().strftime('%H:%M:%S')
    html = f'''<html><head>
<title>Która godzina</title>
</head>
<body style="background-color: #FFFFDD">
<p>Teraz jest godzina <strong style="color:purple">{godzina}</strong></p>
</body>
</html>
'''
    return HttpResponse(html)


def czas_szablon(request:HttpRequest) -> HttpResponse:
    godzina = datetime.now().strftime('%H:%M:%S')
    return render(request=request,
                  template_name='szablon_dla_czasu.html',
                  context={'godz': godzina})

def index(request:HttpRequest) -> HttpResponse:
    return render(request=request, template_name='index.html')


def rozmowa(request:HttpRequest) -> HttpResponse:
    # request.GET zwraca słownik wszystkich parametrów przekazanych w zapytaniu (jako parametry typu GET, czyli w adresie)
    # wartość ze słownika moglibyśmy odczytać pisząc request.GET['imie'], ale w razie braku danych byłby wyjątek KeyError
    # można użyć metody get, która w razie braku danych zwraca None i nie wyrzuca błędu
    imie = request.GET.get('imie')
    if imie:
        powitanie = f'Witaj {imie}!'
    else:
        powitanie = 'Witaj anonimie. Możesz swoje imię...'

    return render(request=request,
                  template_name='rozmowa.html',
                  context={'powitanie': powitanie})


def kalkulator_get(request:HttpRequest) -> HttpResponse:
    parametr1 = request.GET.get('arg1')
    parametr2 = request.GET.get('arg2')
    operacja = request.GET.get('operacja')

    wynik = 0
    if parametr1 and parametr2 and operacja:
        liczba1 = int(parametr1)
        liczba2 = int(parametr2)
        wynik = oblicz(liczba1, liczba2, operacja)

    return render(request=request,
                  template_name='kalkulator_get.html',
                  context={'wynik': wynik})


def kalkulator_post(request:HttpRequest) -> HttpResponse:
    context = {}
    try:
        liczba1 = int(request.POST['arg1'])
        liczba2 = int(request.POST['arg2'])
        operacja = request.POST['operacja']
        context['wynik'] = oblicz(liczba1, liczba2, operacja)
    except KeyError:
        pass
    except ValueError as e:
        context['error'] = f'Niepoprawne dane: {e}'

    return render(request=request,
                  template_name='kalkulator_post.html',
                  context=context)


def oblicz(liczba1:int, liczba2:int, operacja:str) -> int:
    if operacja == '+': return liczba1 + liczba2
    if operacja == '-': return liczba1 - liczba2
    if operacja == '*': return liczba1 * liczba2
    if operacja == '/': return liczba1 // liczba2
    if operacja == '^': return liczba1 ** liczba2
    return 0