# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-26 19:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=8)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('write_at', models.DateTimeField(default=datetime.datetime(2016, 11, 26, 19, 2, 56, 791501, tzinfo=utc))),
                ('publish_at', models.DateTimeField(blank=True, null=True)),
                ('is_visible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('encrypted_password', models.CharField(max_length=256)),
                ('salt', models.CharField(max_length=256)),
                ('encrypt_cycle', models.IntegerField(default=25000)),
                ('is_valid', models.BooleanField(default=False)),
            ],
        ),
    ]