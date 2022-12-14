# Generated by Django 3.1.3 on 2022-07-12 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20220531_1904'),
        ('geofences', '0005_auto_20220428_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeofenceGroup',
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
