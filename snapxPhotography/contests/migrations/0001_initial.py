# Generated by Django 5.1.3 on 2024-11-22 11:42

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('award', models.IntegerField(help_text='Prize amount in currency (e.g., USD), maximum 5 digits', validators=[django.core.validators.MaxLengthValidator(5, message='Please enter a 5 digit number!!!')], verbose_name='Award')),
                ('deadline', models.DateField(help_text='Deadline for contest submissions', verbose_name='Deadline Date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contest', to='categories.category', verbose_name='Category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]