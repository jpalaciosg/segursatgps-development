# Generated by Django 3.1.3 on 2022-11-03 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forwarders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queues',
            name='account',
        ),
    ]