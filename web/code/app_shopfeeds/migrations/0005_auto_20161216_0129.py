# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_shopfeeds', '0004_auto_20161215_1828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datafeed',
            options={'ordering': ['name', 'code'], 'verbose_name': 'Data Feed', 'verbose_name_plural': 'Data Feeds'},
        ),
    ]
