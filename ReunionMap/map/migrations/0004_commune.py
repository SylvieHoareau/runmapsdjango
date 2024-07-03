# Generated by Django 5.0.6 on 2024-07-03 11:39

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("map", "0003_foretpublique"),
    ]

    operations = [
        migrations.CreateModel(
            name="Commune",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nom", models.CharField(max_length=100)),
                ("nom_m", models.CharField(max_length=100)),
                ("insee_com", models.CharField(max_length=10, unique=True)),
                ("statut", models.CharField(max_length=100)),
                ("population", models.IntegerField()),
                ("insee_can", models.CharField(max_length=10)),
                ("insee_arr", models.CharField(max_length=10)),
                ("insee_dep", models.CharField(max_length=10)),
                ("insee_reg", models.CharField(max_length=10)),
                ("insee_epci", models.CharField(max_length=10)),
                (
                    "geometrie",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
        ),
    ]