# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 17:39
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("parties", "0002_auto_20160412_1739"),
        ("people", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="person", name="party_name"),
        migrations.AddField(
            model_name="person",
            name="party",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="parties.Party",
            ),
        ),
    ]
