# Generated by Django 3.1.3 on 2020-12-07 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_is_active'),
        ('alerts', '0004_trigger_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.PositiveIntegerField()),
                ('alert_type', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.account')),
            ],
            options={
                'unique_together': {('alert_type', 'account')},
            },
        ),
    ]
