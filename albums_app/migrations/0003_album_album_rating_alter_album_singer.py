# Generated by Django 5.1.2 on 2024-11-14 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums_app', '0002_album_delete_musician'),
        ('musicians_app', '0002_alter_musician_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_rating',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='album',
            name='singer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='musicians_app.musician'),
        ),
    ]
