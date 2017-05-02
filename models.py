# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from user_auth.models import Bag

# Create your models here.
class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    bag = models.ForeignKey(Bag)
