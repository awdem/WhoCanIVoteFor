# Generated by Django 2.2.20 on 2021-06-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leaflets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leaflet",
            name="thumb_url",
            field=models.URLField(blank=True, max_length=800, null=True),
        ),
    ]
