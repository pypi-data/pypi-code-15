# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-13 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proso_user', '0001_initial'),
        ('proso_subscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='session',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='proso_user.Session'),
        ),
    ]
