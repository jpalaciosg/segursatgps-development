# Generated by Django 3.1.3 on 2021-04-29 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0002_devicedigitaoutput'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
