# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0003_auto_20161204_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftslots',
            name='shiftId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shift.Shifts'),
        ),
    ]
