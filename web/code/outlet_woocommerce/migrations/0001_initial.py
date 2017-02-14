# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-11 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wooProductAttribute',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
                ('wid', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Woo ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('slug', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Slug')),
                ('type', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Type')),
                ('order_by', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Order By')),
                ('has_archives', models.BooleanField(default=False, verbose_name='Has Archives?')),
            ],
            options={
                'verbose_name_plural': 'Product Attributes',
                'verbose_name': 'Product Attribute',
                'ordering': ['store', 'order_by', 'name'],
            },
        ),
        migrations.CreateModel(
            name='wooProductAttributeTerm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
                ('wid', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='Woo ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('slug', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Slug')),
                ('menu_order', models.IntegerField(default=0, verbose_name='Menu Order')),
                ('count', models.IntegerField(default=0, verbose_name='Count')),
                ('wr_tooltip', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='WR Tooltip')),
                ('wr_color', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='WR Color')),
                ('wr_label', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='WR Label')),
                ('productattribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outlet_woocommerce.wooProductAttribute', verbose_name='Product Attribute')),
            ],
            options={
                'verbose_name_plural': 'Product Attribute Terms',
                'verbose_name': 'Product Attribute Term',
                'ordering': ['menu_order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='wooStore',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, default='', help_text='Generally, a two-character uppercase code. Used in SKUs.', max_length=16, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Name')),
                ('base_url', models.URLField(blank=True, default='', help_text="Include the schema and FQDN only (e.g., 'https://example.com'). No trailing slash.", null=True, verbose_name='Base URL')),
                ('consumer_key', models.CharField(blank=True, max_length=43, null=True, verbose_name='Consumer Key')),
                ('consumer_secret', models.CharField(blank=True, max_length=43, null=True, verbose_name='Consumer Secret')),
                ('timezone', timezone_field.fields.TimeZoneField(default='America/New_York')),
                ('verify_ssl', models.BooleanField(default=True, help_text='Uncheck this if you are using a self-signed SSL certificate to disable ssl verification.', verbose_name='Verify SSL?')),
            ],
            options={
                'verbose_name_plural': 'Stores',
                'verbose_name': 'Store',
                'ordering': ['name', 'code'],
            },
        ),
        migrations.AddField(
            model_name='wooproductattribute',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outlet_woocommerce.wooStore'),
        ),
    ]