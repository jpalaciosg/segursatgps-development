# Generated by Django 3.1.3 on 2022-03-28 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_user_description'),
        ('geofences', '0003_geofence_show_geofence_on_map'),
        ('triggers', '0030_auto_20220328_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitTriggerExtension1008',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seconds', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
                ('geofences', models.ManyToManyField(to='geofences.Geofence')),
            ],
        ),
        migrations.AddField(
            model_name='unittrigger',
            name='extension1008',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='triggers.unittriggerextension1008'),
        ),
    ]
