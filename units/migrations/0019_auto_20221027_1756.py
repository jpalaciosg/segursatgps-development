# Generated by Django 3.1.3 on 2022-10-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0018_device_is_replica'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='valve1_source',
            field=models.CharField(default='nothing', max_length=50),
        ),
        migrations.AddField(
            model_name='device',
            name='valve2_source',
            field=models.CharField(default='nothing', max_length=50),
        ),
    ]
