# Generated by Django 5.0.6 on 2024-05-19 15:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_driver_current_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='colis',
            name='image',
            field=models.ImageField(default=1, upload_to='colis_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])]),
            preserve_default=False,
        ),
    ]