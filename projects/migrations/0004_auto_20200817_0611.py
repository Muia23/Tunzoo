# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-17 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_post_techs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='techs',
            field=models.ManyToManyField(blank=True, to='projects.Techs'),
        ),
    ]
