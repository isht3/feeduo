# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_chainswitcher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chainswitcher',
            old_name='relation',
            new_name='customer',
        ),
    ]
