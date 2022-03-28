# Generated by Django 3.1.3 on 2022-03-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0007_osinergminlocation_it_was_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='SutranPointsOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]