# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0002_auto_20170223_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='enable',
            field=models.BooleanField(default=True, verbose_name='启用'),
        ),
    ]
