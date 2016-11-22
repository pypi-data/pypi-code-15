# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_auto_20160419_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='repeated_item_text',
            field=models.CharField(blank=True, help_text="e.g. 'Section home' or 'Overview'. If left blank, the page title will be used.", max_length=255, verbose_name='repeated item link text'),
        ),
        migrations.AlterField(
            model_name='toplevelpage',
            name='repeated_item_text',
            field=models.CharField(blank=True, help_text="e.g. 'Section home' or 'Overview'. If left blank, the page title will be used.", max_length=255, verbose_name='repeated item link text'),
        ),
    ]
