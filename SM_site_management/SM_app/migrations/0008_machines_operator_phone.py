# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-01 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SM_app', '0007_auto_20180301_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='machines',
            name='operator_phone',
            field=models.CharField(default='888-888-888', max_length=64),
        ),
    ]
