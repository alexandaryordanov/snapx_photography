# Generated by Django 5.1.3 on 2024-12-03 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_account_first_name_alter_account_last_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myappuser',
            options={'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
    ]