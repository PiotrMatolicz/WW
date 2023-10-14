from django.contrib import admin

# Ten plik edytujemy, aby w panelu administratora można było edytować produkty.

# Z bieżącego pakietu (czyli katalogu), z modułu (czyli pliku) models zaimportuj definicję klasy Produkt
from .models import Produkt
# lub: from sklep.models import Produkt
# lub: from sklep.models import *

admin.site.register(Produkt)
