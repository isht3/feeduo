# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 10:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0002_auto_20170703_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chain',
            options={'ordering': ('name',)},
        ),
    ]
