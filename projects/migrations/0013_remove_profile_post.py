# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-08-18 04:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
    ]
