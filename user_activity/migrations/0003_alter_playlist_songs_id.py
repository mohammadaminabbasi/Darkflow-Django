# Generated by Django 4.0.1 on 2022-06-30 06:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_activity', '0002_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='songs_id',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), size=None),
        ),
    ]