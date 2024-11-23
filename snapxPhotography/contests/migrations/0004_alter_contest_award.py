# Generated by Django 5.1.3 on 2024-11-23 15:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_contest_requirements_alter_contest_award_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='award',
            field=models.PositiveIntegerField(help_text='Prize amount in currency (e.g., USD), maximum 5 digits', validators=[django.core.validators.MaxValueValidator(9999, message='Please enter a 4 digit number!!!')], verbose_name='Award'),
        ),
    ]
