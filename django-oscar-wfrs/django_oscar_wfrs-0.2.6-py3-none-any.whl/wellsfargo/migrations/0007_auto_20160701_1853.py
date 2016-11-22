# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellsfargo', '0006_auto_20160701_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='financingplan',
            options={'ordering': ('plan_number',)},
        ),
        migrations.AddField(
            model_name='financingplanbenefit',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
