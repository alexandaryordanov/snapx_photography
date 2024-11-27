# Generated by Django 5.1.3 on 2024-11-27 21:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0002_alter_photo_options_photo_vote'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='photos.photo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'photo')},
            },
        ),
    ]
