# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-14 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_car_manufacturers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='manufacturers',
        ),
    ]
