# Generated by Django 5.1.3 on 2024-11-27 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
    ]
