# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-03 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0022_auto_20180903_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.BigIntegerField(default=0),
        ),
    ]
