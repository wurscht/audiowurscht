# Generated by Django 2.2.3 on 2019-07-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song',
            field=models.FileField(default=None, upload_to='songs/'),
            preserve_default=False,
        ),
    ]
