# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 11:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20170703_0744'),
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChainSwitcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('switcher', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('relation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='switcher', to='customer.Customer')),
            ],
        ),
    ]
