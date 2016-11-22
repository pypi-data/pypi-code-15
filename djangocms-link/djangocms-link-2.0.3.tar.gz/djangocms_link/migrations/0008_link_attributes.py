# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 20:45
from __future__ import unicode_literals

from django.db import migrations
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_link', '0007_set_related_name_for_cmsplugin_ptr'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, help_text='Optional. Link HTML tag attributes', verbose_name='link tag attributes'),
        ),
    ]
