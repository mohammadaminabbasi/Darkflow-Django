# Generated by Django 4.0.1 on 2022-01-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songsapi', '0003_dfsong_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='songembedding',
            name='row_number',
            field=models.IntegerField(default=-1),
        ),
    ]
