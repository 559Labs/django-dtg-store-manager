# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_manufactureritemfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufactureritemdimension',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is Active?'),
        ),
        migrations.AddField(
            model_name='manufactureritemdimension',
            name='manufacturer_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.ManufacturerItem'),
        ),
        migrations.AddField(
            model_name='manufactureritemfile',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is Active?'),
        ),
    ]
