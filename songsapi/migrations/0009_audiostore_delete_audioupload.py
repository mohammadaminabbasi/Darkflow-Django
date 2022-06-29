# Generated by Django 4.0.1 on 2022-06-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songsapi', '0008_audioupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.FileField(upload_to='documents/')),
            ],
            options={
                'db_table': 'Audio_store',
            },
        ),
        migrations.DeleteModel(
            name='AudioUpload',
        ),
    ]