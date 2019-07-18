# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Venue(models.Model):
    google_id = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.id, self.google_id, self.name, self.lat, self.long)

class Show(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    event_url = models.CharField(max_length=255)
    date = models.DateTimeField(null=False)
    poster_url = models.CharField(max_length=255)
    venue_name = models.CharField(max_length=255, null=False)
    venue_google_id = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.name, self.description, self.event_url, self.date, self.poster_url, self.venue_name, self.venue_google_id)

# Create your models here.
