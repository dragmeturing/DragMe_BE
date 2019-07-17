# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Venue
from .models import Show

admin.site.register(Venue)
admin.site.register(Show)

# Register your models here.
