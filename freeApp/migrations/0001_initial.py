# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-20 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sightings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('city', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('shape', models.TextField(blank=True, null=True)),
                ('duration_seconds_field', models.IntegerField(blank=True, db_column='duration (seconds)', null=True)),
                ('duration_hours_min_field', models.TextField(blank=True, db_column='duration (hours/min)', null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('date_posted', models.DateField()),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sightings',
                'managed': False,
            },
        ),
    ]
