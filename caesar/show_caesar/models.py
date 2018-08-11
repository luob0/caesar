# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Transaction(models.Model):
    tradeid = models.PositiveIntegerField(default=0)
    module = models.PositiveSmallIntegerField(default=0)
    test = models.BooleanField(default=0)
    truth = models.BooleanField(default=0)

class Data(models.Model):
    accuracy = models.FloatField(default=0)
    precision = models.FloatField(default=0)
    recall = models.FloatField(default=0)
    disturb = models.FloatField(default=0)
