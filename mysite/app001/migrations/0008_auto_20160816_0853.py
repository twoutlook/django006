# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0007_auto_20160816_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='item002',
            name='field6',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item004',
            name='field6',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
