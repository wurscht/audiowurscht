# Generated by Django 2.2.3 on 2019-08-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_remove_song_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='tracknumber',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
