# Generated by Django 3.1.3 on 2022-10-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0017_device_show_unit_datetime_in_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='is_replica',
            field=models.BooleanField(default=False),
        ),
    ]
