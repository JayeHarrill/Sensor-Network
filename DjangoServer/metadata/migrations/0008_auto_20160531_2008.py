# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-01 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0007_auto_20160517_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancelog',
            name='activity',
            field=models.TextField(default='Tightening Gland Follower'),
        ),
    ]
