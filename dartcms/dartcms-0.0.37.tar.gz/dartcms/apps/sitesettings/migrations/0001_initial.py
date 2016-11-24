# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 15:04
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='Identifier')),
                ('description', models.TextField(default=b'', verbose_name='Description')),
                ('type', models.CharField(blank=True, choices=[(b'text', 'String'), (b'textarea', 'Text'), (b'rich', 'Rich Editor'), (b'select', 'Select'), (b'date', 'Date'), (b'file', 'File')], default=b'text', max_length=10, verbose_name='Type')),
                ('text_value', models.TextField(blank=True, default=b'', verbose_name='Value for text type')),
                ('date_value', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Value for date type')),
                ('file_value', models.FileField(blank=True, null=True, upload_to=b'vars', verbose_name='Value for file')),
                ('options', models.TextField(blank=True, default=b'', verbose_name='Options for select type (use ";" as separator)')),
            ],
            options={
                'ordering': ['slug'],
                'verbose_name': 'Site setting',
                'verbose_name_plural': 'Site settings',
            },
        ),
    ]
