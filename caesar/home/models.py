# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Account(models.Model):
    account = models.PositiveIntegerField(default=0)
    passwd = models.PositiveIntegerField(default=0)
