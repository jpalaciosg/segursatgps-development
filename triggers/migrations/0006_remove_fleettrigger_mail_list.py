# Generated by Django 3.1.3 on 2022-03-19 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('triggers', '0005_fleettriggerextension1004_fleettriggerextension1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fleettrigger',
            name='mail_list',
        ),
    ]
