# Generated by Django 3.1.3 on 2022-03-26 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_user_description'),
        ('geofences', '0003_geofence_show_geofence_on_map'),
        ('triggers', '0015_auto_20220326_1238'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FleetTriggerExtension1007',
            new_name='Extension1007',
        ),
    ]
