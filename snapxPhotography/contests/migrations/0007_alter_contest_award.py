# Generated by Django 5.1.3 on 2024-12-01 14:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0006_alter_contest_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='award',
            field=models.PositiveIntegerField(help_text='Prize amount in currency (e.g., USD), 4 digits', validators=[django.core.validators.MaxValueValidator(9999, message='Please enter a 4 digit number!!!'), django.core.validators.MinValueValidator(1000, message='Please enter a 4 digit number!!!')], verbose_name='Award'),
        ),
    ]
