# Generated by Django 3.1.3 on 2022-10-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0016_device_last_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='show_unit_datetime_in_map',
            field=models.BooleanField(default=False),
        ),
    ]
