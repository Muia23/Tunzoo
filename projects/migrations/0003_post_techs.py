# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-17 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_techs'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='techs',
            field=models.ManyToManyField(to='projects.Techs'),
        ),
    ]