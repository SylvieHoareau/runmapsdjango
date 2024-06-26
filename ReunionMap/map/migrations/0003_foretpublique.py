# Generated by Django 5.0.6 on 2024-06-28 13:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("map", "0002_randonnee_delete_pointofinterest"),
    ]

    operations = [
        migrations.CreateModel(
            name="ForetPublique",
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
                ("cleabs", models.CharField(max_length=255, unique=True)),
                ("nature", models.CharField(max_length=255)),
                ("toponyme", models.CharField(max_length=255)),
                ("statut_du_toponyme", models.CharField(max_length=255)),
                ("importance", models.IntegerField()),
                ("date_creation", models.IntegerField()),
                ("date_modification", models.DateTimeField()),
                ("date_de_confirmation", models.DateTimeField()),
                ("sources", models.CharField(max_length=255)),
                ("identifiants_sources", models.CharField(max_length=255)),
                (
                    "methode_d_acquisition_planimetrique",
                    models.CharField(max_length=255),
                ),
                ("precision_plainmetrique", models.FloatField()),
                (
                    "geometrie",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
        ),
    ]
