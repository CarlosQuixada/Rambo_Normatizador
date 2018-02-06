# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Normatizador (models.Model):
    text = models.CharField(max_length=255)

