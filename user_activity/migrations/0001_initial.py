# Generated by Django 4.0.1 on 2022-06-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SongComments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('song_id', models.CharField(max_length=250)),
                ('user_id', models.CharField(max_length=250)),
                ('comment', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SongLikes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('song_id', models.CharField(max_length=250)),
                ('user_id', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SongListens',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('song_id', models.CharField(max_length=250)),
                ('user_id', models.CharField(max_length=250)),
                ('count', models.IntegerField(default=1)),
            ],
        ),
    ]
