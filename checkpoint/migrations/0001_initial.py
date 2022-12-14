# Generated by Django 3.1.3 on 2022-08-09 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geofences', '0006_geofencegroup'),
        ('users', '0024_auto_20220531_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
                ('geofences', models.ManyToManyField(to='geofences.Geofence')),
            ],
        ),
    ]
