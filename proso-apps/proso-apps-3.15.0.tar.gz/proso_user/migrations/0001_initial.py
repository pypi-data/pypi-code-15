# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-01 07:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=50, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'classes',
            },
        ),
        migrations.CreateModel(
            name='HttpUserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('content_hash', models.CharField(db_index=True, max_length=40, unique=True)),
                ('device_family', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('os_family', models.CharField(blank=True, default=None, max_length=39, null=True)),
                ('os_version', models.CharField(blank=True, default=None, max_length=39, null=True)),
                ('browser_family', models.CharField(blank=True, default=None, max_length=39, null=True)),
                ('browser_version', models.CharField(blank=True, default=None, max_length=39, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, default=None, max_length=39, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('display_width', models.IntegerField(blank=True, default=None, null=True)),
                ('display_height', models.IntegerField(blank=True, default=None, null=True)),
                ('http_user_agent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='proso_user.HttpUserAgent')),
                ('location', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='proso_user.Location')),
            ],
        ),
        migrations.CreateModel(
            name='TimeZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('content_hash', models.CharField(db_index=True, max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_emails', models.BooleanField(default=True)),
                ('public', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
                ('value', models.CharField(max_length=200)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proso_user.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.SlugField()),
                ('lang', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('answer_type', models.CharField(choices=[('c', 'closed'), ('m', 'mixed'), ('o', 'open')], default='o', max_length=1)),
                ('repeat', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_answer', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestionCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuestionPossibleAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.SlugField()),
                ('active', models.BooleanField(default=True)),
                ('content', models.CharField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='possible_answers', to='proso_user.UserQuestion')),
            ],
        ),
        migrations.AddField(
            model_name='userquestionanswer',
            name='closed_answer',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proso_user.UserQuestionPossibleAnswer'),
        ),
        migrations.AddField(
            model_name='userquestionanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='proso_user.UserQuestion'),
        ),
        migrations.AddField(
            model_name='userquestionanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userquestion',
            name='conditions',
            field=models.ManyToManyField(to='proso_user.UserQuestionCondition'),
        ),
        migrations.AddField(
            model_name='userquestion',
            name='on_events',
            field=models.ManyToManyField(to='proso_user.UserQuestionEvent'),
        ),
        migrations.AddField(
            model_name='session',
            name='time_zone',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='proso_user.TimeZone'),
        ),
        migrations.AddField(
            model_name='session',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='class',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='classes', to='proso_user.UserProfile'),
        ),
        migrations.AddField(
            model_name='class',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_classes', to='proso_user.UserProfile'),
        ),
    ]
