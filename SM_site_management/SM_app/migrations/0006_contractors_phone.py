# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-28 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SM_app', '0005_sites_status_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractors',
            name='phone',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
