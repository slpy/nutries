# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-03 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0023_auto_20180903_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
