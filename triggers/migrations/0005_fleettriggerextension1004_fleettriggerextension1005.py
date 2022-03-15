# Generated by Django 3.1.3 on 2022-03-15 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_user_description'),
        ('geofences', '0003_geofence_show_geofence_on_map'),
        ('triggers', '0004_fleettrigger_mail_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='FleetTriggerExtension1005',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
                ('geofences', models.ManyToManyField(to='geofences.Geofence')),
            ],
        ),
        migrations.CreateModel(
            name='FleetTriggerExtension1004',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
                ('geofences', models.ManyToManyField(to='geofences.Geofence')),
            ],
        ),
    ]