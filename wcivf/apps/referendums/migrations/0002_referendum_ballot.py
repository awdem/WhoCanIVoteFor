# Generated by Django 2.2.24 on 2021-09-10 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("elections", "0034_update_ordering"),
        ("referendums", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="referendum",
            name="ballot",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="elections.PostElection",
            ),
        ),
    ]
