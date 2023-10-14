from django.db import models

# ORM
# Create your models here.

class Produkt(models.Model):
    nazwa = models.CharField(max_length=100) # varchar
    cena = models.DecimalField(max_digits=10, decimal_places=2) # numeric / number / decimal
    termin_waznosci = models.DateField()
    promocja = models.BooleanField()
