# Generated by Django 3.1.3 on 2022-03-21 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triggers', '0010_auto_20220321_2201'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fleettrigger',
            unique_together=set(),
        ),
    ]