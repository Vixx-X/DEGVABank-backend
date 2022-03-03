# Generated by Django 4.0.1 on 2022-03-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_alter_creditcard_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='credit_limit',
            field=models.DecimalField(decimal_places=2, default=50000.0, max_digits=12, verbose_name='credit limit'),
        ),
    ]