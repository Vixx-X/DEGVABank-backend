# Generated by Django 4.0.1 on 2022-03-01 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PayWayMetaData",
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
                ("app_id", models.SlugField(unique=True, verbose_name="app id")),
                ("app_name", models.CharField(max_length=255, verbose_name="app name")),
                ("backend", models.URLField(verbose_name="backend endpoint")),
                ("success", models.URLField(verbose_name="success url")),
                ("fail", models.URLField(verbose_name="fail url")),
                (
                    "date_created",
                    models.DateField(
                        auto_now_add=True, db_index=True, verbose_name="date created"
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.account",
                        verbose_name="owner account",
                    ),
                ),
            ],
            options={
                "verbose_name": "pay way meta data",
                "verbose_name_plural": "pay way meta data",
                "db_table": "payway_metadata",
            },
        ),
        migrations.CreateModel(
            name="PayWayKeys",
            fields=[
                (
                    "public",
                    models.CharField(
                        editable=False,
                        max_length=64,
                        primary_key=True,
                        serialize=False,
                        verbose_name="publishable key",
                    ),
                ),
                ("private", models.CharField(max_length=64, verbose_name="secret key")),
                (
                    "meta_data",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="keys",
                        to="payway.paywaymetadata",
                    ),
                ),
            ],
            options={
                "verbose_name": "pay way key",
                "verbose_name_plural": "pay way keys",
                "db_table": "payway_keys",
            },
        ),
    ]
