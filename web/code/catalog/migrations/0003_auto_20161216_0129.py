# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_item_product_label_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturerfilelibraryitem',
            name='dpi',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='DPI'),
        ),
        migrations.AlterField(
            model_name='manufacturerfilelibraryitem',
            name='size',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='manufacturerfilelibraryitem',
            name='width',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Width'),
        ),
    ]
