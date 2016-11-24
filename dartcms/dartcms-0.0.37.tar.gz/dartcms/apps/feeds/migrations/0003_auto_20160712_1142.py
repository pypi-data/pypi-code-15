# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 11:42
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20160706_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeditem',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feeds.Feed', verbose_name='Feed'),
        ),
        migrations.AlterField(
            model_name='feeditem',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=b'feeds/%Y/%m/%d', verbose_name='Picture'),
        ),
    ]
