# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_printful', '0014_auto_20170212_1512'),
        ('business', '0006_bzcreativecollection_bzbrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='bzCreativeRendering',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('bzcreativedesign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.bzCreativeDesign', verbose_name='Design')),
                ('bzcreativelayout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.bzCreativeLayout', verbose_name='Layout')),
                ('pfcatalogfilespec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfCatalogFileSpec', verbose_name='Spec')),
                ('pfprintfile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor_printful.pfPrintFile', verbose_name='Print File')),
            ],
            options={
                'verbose_name_plural': 'Creative Layouts',
                'verbose_name': 'Creative Layout',
            },
        ),
    ]