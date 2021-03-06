# Generated by Django 4.0.1 on 2022-03-01 23:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("C2C", "error (credit card to credit card)"),
                            ("C2A", "from credit card to account"),
                            ("A2C", "from account to credit card"),
                            ("A2A", "from account to account"),
                        ],
                        max_length=4,
                        verbose_name="transaction type",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ERR", "error"),
                            ("PEN", "pending"),
                            ("ACC", "accepted"),
                            ("REJ", "rejected"),
                        ],
                        default="PEN",
                        max_length=4,
                        verbose_name="transaction status",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=12, verbose_name="amount of money"
                    ),
                ),
                (
                    "reason",
                    models.CharField(
                        max_length=50,
                        verbose_name="reason why the transaction is being carried out",
                    ),
                ),
                (
                    "date",
                    models.DateField(auto_now=True, verbose_name="transaction date"),
                ),
                (
                    "target",
                    models.CharField(
                        max_length=20,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="not a valid account or credit card",
                                regex="^(\\d{16}|\\d{20})$",
                            )
                        ],
                        verbose_name="target account or credit card number",
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        max_length=20,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="not a valid account or credit card",
                                regex="^(\\d{16}|\\d{20})$",
                            )
                        ],
                        verbose_name="source account or credit card number",
                    ),
                ),
            ],
            options={
                "verbose_name": "transaction",
                "verbose_name_plural": "transactions",
                "db_table": "transactions",
            },
        ),
    ]
