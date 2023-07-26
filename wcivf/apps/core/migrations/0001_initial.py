# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 16:31
from __future__ import unicode_literals

import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LoggedPostcode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("postcode", models.CharField(max_length=100)),
                (
                    "utm_source",
                    models.CharField(blank=True, db_index=True, max_length=100),
                ),
                (
                    "utm_medium",
                    models.CharField(blank=True, db_index=True, max_length=100),
                ),
                (
                    "utm_campaign",
                    models.CharField(blank=True, db_index=True, max_length=100),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
                "ordering": ("-modified", "-created"),
            },
        )
    ]
