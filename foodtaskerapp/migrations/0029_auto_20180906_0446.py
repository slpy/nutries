# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-06 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0028_auto_20180906_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='sub_total',
            field=models.IntegerField(),
        ),
    ]
