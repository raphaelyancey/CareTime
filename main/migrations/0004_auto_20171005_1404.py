# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-05 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171005_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='pickup_time',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_time',
            field=models.TimeField(),
        ),
    ]