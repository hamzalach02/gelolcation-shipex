# Generated by Django 5.0.6 on 2024-05-18 22:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_colis_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cin', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
                ('license_number', models.CharField(max_length=255)),
                ('vehicle_number', models.CharField(max_length=255)),
            ],
        ),
    ]