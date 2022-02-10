# Generated by Django 4.0.1 on 2022-02-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True, help_text='account should be used by owner?', verbose_name='account is active'),
        ),
    ]
