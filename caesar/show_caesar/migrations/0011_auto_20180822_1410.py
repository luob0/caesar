# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-22 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_caesar', '0010_trade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='a',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trade',
            name='p',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trade',
            name='r',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trade',
            name='s',
            field=models.SmallIntegerField(default=0),
        ),
    ]
