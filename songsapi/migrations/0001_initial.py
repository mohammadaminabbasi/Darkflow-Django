# Generated by Django 4.0.1 on 2022-06-04 19:41

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DFArtist',
            fields=[
                ('name', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('imageUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='DFSong',
            fields=[
                ('id', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('artist', models.CharField(default='', max_length=1000)),
                ('songUrl', models.URLField()),
                ('imageUrl', models.URLField()),
                ('lyric', models.TextField(null=True)),
                ('genre', models.CharField(default='', max_length=100)),
            ],
        ),
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
            name='RecommendedSongs',
            fields=[
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='songsapi.dfsong', unique=True)),
                ('recommends_songs_id', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), size=None)),
            ],
        ),
    ]
