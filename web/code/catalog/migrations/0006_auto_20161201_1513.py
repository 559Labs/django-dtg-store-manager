# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20161201_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturervariant',
            name='shipping_ca',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Shipping (Canada)'),
        ),
        migrations.AddField(
            model_name='manufacturervariant',
            name='shipping_ca_addl',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Shipping (Canada) - Additional Item'),
        ),
        migrations.AddField(
            model_name='manufacturervariant',
            name='shipping_us',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Shipping (USA)'),
        ),
        migrations.AddField(
            model_name='manufacturervariant',
            name='shipping_us_addl',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Shipping (USA) - Additional Item'),
        ),
        migrations.AddField(
            model_name='manufacturervariant',
            name='shipping_ww',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Shipping (Worldwide)'),
        ),
        migrations.AddField(
            model_name='manufacturervariant',
            name='shipping_ww_addl',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Shipping (Worldwide) - Additional Item'),
        ),
    ]
