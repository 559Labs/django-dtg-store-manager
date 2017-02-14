# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_printful', '0011_auto_20170212_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pfcatalogsize',
            options={'ordering': ['sort_group', 'sort_order', 'label'], 'verbose_name': 'Catalog Size', 'verbose_name_plural': 'Catalog Size'},
        ),
        migrations.AddField(
            model_name='pfcatalogsize',
            name='sort_group',
            field=models.CharField(blank=True, default='', max_length=2, null=True, verbose_name='Sort Group'),
        ),
        migrations.AlterField(
            model_name='pfcatalogproduct',
            name='is_active',
            field=models.BooleanField(default=True, help_text='', verbose_name='Is Active?'),
        ),
    ]