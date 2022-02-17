# Generated by Django 4.0.1 on 2022-02-10 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('+ACCOUNT', 'open a new account'), ('+CC', 'create a credit card'), ('+DC', 'create a dedit card')], max_length=15, verbose_name='reason')),
                ('status', models.CharField(choices=[('APPROVED', 'Approved'), ('PENDING', 'Pending'), ('DENIED', 'Denied')], default='PENDING', help_text='status (approved, pending, denied)', max_length=10, verbose_name='status')),
                ('date_processed', models.DateField(auto_now=True, db_index=True, verbose_name='date processed')),
                ('date_created', models.DateField(auto_now_add=True, db_index=True, verbose_name='date created')),
                ('object_id', models.CharField(max_length=20)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='petitions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'petition',
                'verbose_name_plural': 'petitions',
                'db_table': 'petitions',
            },
        ),
    ]