# Generated by Django 3.1.3 on 2022-03-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertMailQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_name', models.CharField(max_length=50)),
                ('alert_description', models.TextField(blank=True)),
                ('alert_timestamp', models.IntegerField()),
                ('alert_speed', models.IntegerField()),
                ('alert_angle', models.IntegerField()),
                ('alert_address', models.TextField(blank=True)),
                ('unit_name', models.CharField(max_length=50)),
                ('unit_description', models.CharField(max_length=50)),
                ('account_id', models.IntegerField()),
                ('customer_description', models.TextField(blank=True)),
                ('mails', models.TextField(blank=True)),
                ('it_was_sent', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='alertmailqueue',
            index=models.Index(fields=['account_id', 'alert_timestamp'], name='mails_alert_account_b17f0a_idx'),
        ),
    ]
