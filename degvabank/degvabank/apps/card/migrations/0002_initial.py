# Generated by Django 4.0.1 on 2022-02-10 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('card', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='credit_cards', to=settings.AUTH_USER_MODEL, verbose_name='card owner'),
        ),
    ]