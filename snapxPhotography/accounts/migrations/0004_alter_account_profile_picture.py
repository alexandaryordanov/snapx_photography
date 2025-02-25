# Generated by Django 5.1.3 on 2024-11-16 16:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_picture'),
        ),
    ]
