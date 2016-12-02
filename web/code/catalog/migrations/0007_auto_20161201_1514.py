# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20161201_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='shipping_ca',
        ),
        migrations.RemoveField(
            model_name='item',
            name='shipping_ca_addl',
        ),
        migrations.RemoveField(
            model_name='item',
            name='shipping_us',
        ),
        migrations.RemoveField(
            model_name='item',
            name='shipping_us_addl',
        ),
        migrations.RemoveField(
            model_name='item',
            name='shipping_ww',
        ),
        migrations.RemoveField(
            model_name='item',
            name='shipping_ww_addl',
        ),
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Weight (OZ)'),
        ),
    ]
