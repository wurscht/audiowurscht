# Generated by Django 2.2.3 on 2019-08-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(upload_to='media/profile_pictures'),
        ),
    ]
