# Generated by Django 2.2.3 on 2019-08-14 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20190814_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='date',
        ),
    ]
