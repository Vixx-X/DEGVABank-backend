# Generated by Django 4.0.1 on 2022-02-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'transaction', 'verbose_name_plural': 'transactions'},
        ),
        migrations.AlterModelTable(
            name='transaction',
            table='transactions',
        ),
    ]