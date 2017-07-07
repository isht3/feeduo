# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 10:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20170707_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='number',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
