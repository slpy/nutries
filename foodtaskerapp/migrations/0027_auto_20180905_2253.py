# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-05 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0026_auto_20180905_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='sub_total',
            field=models.FloatField(),
        ),
    ]
