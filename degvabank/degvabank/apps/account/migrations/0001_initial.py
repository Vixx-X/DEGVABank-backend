# Generated by Django 4.0.1 on 2022-02-03 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CHECKING', 'Checking'), ('SAVING', 'Saving')], max_length=10, verbose_name='type of account (checking, saving)')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='account balance')),
                ('creation_date', models.DateField(auto_now=True, verbose_name='creation date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
