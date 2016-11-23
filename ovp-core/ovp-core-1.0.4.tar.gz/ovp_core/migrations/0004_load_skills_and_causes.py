# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 01:14
from __future__ import unicode_literals

from django.db import migrations

skills = ['Arts/Handcrafting', 'Communication', 'Dance/Music', 'Law', 'Education', 'Sports', 'Cooking', 'Management', 'Idioms', 'Computers/Technology', 'Health', 'Others']
causes = ['Professional Training', 'Fight Poverty', 'Conscious consumption', 'Culture, Sport and Art', 'Human Rights', 'Education', 'Youth', 'Elders', 'Environment', 'Citizen Participation', 'Animal Protection', 'Health', 'People with disabilities']


def load_data(apps, schema_editor):
  Skill = apps.get_model("ovp_core", "Skill")
  Cause = apps.get_model("ovp_core", "Cause")

  for skill in skills:
    s = Skill(name=skill)
    s.save()

  for cause in causes:
    c = Cause(name=cause)
    c.save()

def unload_data(apps, schema_editor): #pragma: no cover
  Skill = apps.get_model("ovp_core", "Skill")
  Cause = apps.get_model("ovp_core", "Cause")

  for skill in skills:
    s = Skill.objects.filter(name=skill)
    s.delete()

  for cause in causes:
    c = Cause.objects.filter(name=cause)
    c.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('ovp_core', '0003_cause_skill'),
    ]

    operations = [
        migrations.RunPython(load_data, reverse_code=unload_data)
    ]
