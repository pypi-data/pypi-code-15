# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djmessenger', '0013_auto_20160829_0510'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sending',
            new_name='Reply',
        ),
        migrations.AlterModelTable(
            name='reply',
            table='djm_reply',
        ),
    ]
