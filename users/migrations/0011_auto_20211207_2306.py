# Generated by Django 3.1.3 on 2021-12-07 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20211207_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='view_group_mileage_report',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='view_group_speed_report',
            field=models.BooleanField(default=False),
        ),
    ]
