# Generated by Django 2.2.3 on 2019-08-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190730_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song',
            new_name='path',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='date',
            field=models.IntegerField(default=666),
        ),
        migrations.AddField(
            model_name='song',
            name='tracknumber',
            field=models.IntegerField(default=666),
        ),
    ]
