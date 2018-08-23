# -*- coding: utf-8 -*-

from django.db import models


class Trade(models.Model):
    tradeid = models.PositiveIntegerField(default=0)
    test = models.PositiveSmallIntegerField(default=0)
    truth = models.PositiveSmallIntegerField(default=0)
    module = models.PositiveSmallIntegerField(default=0)
    p = models.SmallIntegerField(default=0)
    r = models.SmallIntegerField(default=0)
    s = models.SmallIntegerField(default=0)
    a = models.SmallIntegerField(default=0)
    accuracy = models.FloatField(default=0)
    precision = models.FloatField(default=0)
    recall = models.FloatField(default=0)
    disturb = models.FloatField(default=0)

# Create your models here.
'''
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

class ModuleS(models.Model):
    sid = models.PositiveIntegerField(default=0)
    test = models.BooleanField(default=0)
    truth = models.BooleanField(default=0)

class ModuleA(models.Model):
    aid = models.PositiveIntegerField(default=0)
    test = models.BooleanField(default=0)
    truth = models.BooleanField(default=0)

class ModuleR(models.Model):
    rid = models.PositiveIntegerField(default=0)
    test = models.BooleanField(default=0)
    truth = models.BooleanField(default=0)

class ModuleP(models.Model):
    pid = models.PositiveIntegerField(default=0)
    test = models.BooleanField(default=0)
    truth = models.BooleanField(default=0)
'''

class CaesarData(models.Model):
    caesarid = models.CharField(max_length=30, null=True)
    cardnum = models.CharField(max_length=50, null=True)
    dmxind01 = models.CharField(max_length=20, null=True)
    dmx10bytestring01 = models.CharField(max_length=20, null=True)
    dmx2bytestring02 = models.CharField(max_length=20, null=True)
    rqotrantimealt = models.CharField(max_length=50, null=True)
    tcaclientamt = models.CharField(max_length=50, null=True)
    rua20bytestring001 = models.CharField(max_length=50, null=True)
    ruaind004 = models.CharField(max_length=20, null=True)
    dmxind03 = models.CharField(max_length=20, null=True)
    sign = models.CharField(max_length=20, null=True)
