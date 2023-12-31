# Generated by Django 4.2.5 on 2023-10-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produkt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nazwa", models.CharField(max_length=100)),
                ("cena", models.DecimalField(decimal_places=2, max_digits=10)),
                ("termin_waznosci", models.DateField()),
                ("promocja", models.BooleanField()),
            ],
        ),
    ]
