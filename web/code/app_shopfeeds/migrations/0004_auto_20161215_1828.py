# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shopfeeds', '0003_datafeed_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafeeditem',
            name='age_group',
            field=models.CharField(blank=True, default='', max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='datafeeditem',
            name='availability',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='datafeeditem',
            name='condition',
            field=models.CharField(blank=True, default='', max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='datafeeditem',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=70, null=True),
        ),
    ]
