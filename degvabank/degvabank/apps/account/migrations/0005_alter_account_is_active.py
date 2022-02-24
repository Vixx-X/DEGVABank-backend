# Generated by Django 4.0.1 on 2022-02-24 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_account_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(db_index=True, default=False, help_text='account should be used by owner?', verbose_name='account is active'),
        ),
    ]