# Generated by Django 5.0.6 on 2024-07-15 07:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("map", "0006_alter_commune_insee_arr_alter_commune_insee_can_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="foretpublique",
            old_name="precision_plainmetrique",
            new_name="precision_planimetrique",
        ),
    ]
