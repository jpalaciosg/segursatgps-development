# Generated by Django 3.1.3 on 2021-04-03 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.CharField(max_length=20, unique=True)),
                ('imei', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('sim_phonenumber', models.CharField(blank=True, max_length=20)),
                ('sim_iccid', models.CharField(blank=True, max_length=20)),
                ('odometer', models.FloatField(default=0.0)),
                ('last_timestamp', models.IntegerField(default=0)),
                ('last_latitude', models.FloatField(default=0)),
                ('last_longitude', models.FloatField(default=0)),
                ('last_altitude', models.IntegerField(default=0)),
                ('last_speed', models.IntegerField(default=-1)),
                ('last_angle', models.IntegerField(default=0)),
                ('last_attributes', models.TextField(blank=True, default='')),
                ('last_address', models.TextField(blank=True, default='')),
                ('previous_location', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
            ],
            options={
                'unique_together': {('name', 'account')},
            },
        ),
        migrations.CreateModel(
            name='DeviceDigitalInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.PositiveIntegerField()),
                ('input_event', models.CharField(choices=[('IGNITION', 'IGNITION'), ('PANIC', 'PANIC')], max_length=50)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.device')),
            ],
            options={
                'unique_together': {('device', 'input', 'input_event')},
            },
        ),
    ]
