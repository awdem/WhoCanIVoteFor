# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 13:35
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("elections", "0007_auto_20160405_0857")]

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("ynr_id", models.CharField(db_index=True, max_length=255)),
                ("name", models.CharField(blank=True, max_length=255)),
                ("email", models.EmailField(max_length=254, null=True)),
                (
                    "gender",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("birth_date", models.CharField(max_length=255, null=True)),
                (
                    "photo",
                    models.ImageField(null=True, upload_to="people/photos"),
                ),
                ("party_name", models.CharField(blank=True, max_length=255)),
                ("elections", models.ManyToManyField(to="elections.Election")),
            ],
        ),
        migrations.CreateModel(
            name="PersonPost",
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
                ("list_position", models.IntegerField(blank=True, null=True)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="people.Person",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="elections.Post",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="person",
            name="posts",
            field=models.ManyToManyField(
                through="people.PersonPost", to="elections.Post"
            ),
        ),
    ]
