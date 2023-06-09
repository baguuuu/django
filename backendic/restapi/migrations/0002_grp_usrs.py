# Generated by Django 4.1.7 on 2023-03-16 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("restapi", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Grp",
            fields=[
                ("idgrp", models.IntegerField(primary_key=True, serialize=False)),
                ("namegrp", models.CharField(max_length=255)),
                ("islast", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Usrs",
            fields=[
                ("idusr", models.IntegerField(primary_key=True, serialize=False)),
                ("nameusr", models.CharField(max_length=255)),
                (
                    "idgrp",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="restapi.grp",
                    ),
                ),
            ],
        ),
    ]
