# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Show
from .models import Venue

admin.site.register(Show)
admin.site.register(Venue)

# Register your models here.
