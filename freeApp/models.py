# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.







class Sightings(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    shape = models.TextField(blank=True, null=True)
    duration_seconds_field = models.IntegerField(db_column='duration (seconds)', blank=True,null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    duration_hours_min_field = models.TextField(db_column='duration (hours/min)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it endedwith '_'.
    comments = models.TextField(blank=True, null=True)
    date_posted = models.DateField() # Field renamed to remove unsuitable characters.
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.comments

    class Meta:
        managed = False
        db_table = 'sightings'

    class ReportBuilder:
        exclude = ('id')  # Lists or tuple of excluded fields
        fields = ('city','state','datetime')   # Explicitly allowed fields
        extra = () 