# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-27 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=64)),
                ('mail', models.EmailField(max_length=254)),
                ('photo', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Contractors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(max_length=64)),
                ('operator', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
                ('unit', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ProvidersMaterials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM_app.Materials')),
                ('providers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM_app.Providers')),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('status', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SitesContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(max_length=64)),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM_app.Contacts')),
                ('sites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM_app.Sites')),
            ],
        ),
        migrations.CreateModel(
            name='SitesMaterials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM_app.Materials')),
                ('sites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM_app.Sites')),
            ],
        ),
        migrations.AddField(
            model_name='materials',
            name='providers',
            field=models.ManyToManyField(through='SM_app.ProvidersMaterials', to='SM_app.Providers'),
        ),
        migrations.AddField(
            model_name='materials',
            name='sites',
            field=models.ManyToManyField(through='SM_app.SitesMaterials', to='SM_app.Sites'),
        ),
        migrations.AddField(
            model_name='machines',
            name='sites',
            field=models.ManyToManyField(to='SM_app.Sites'),
        ),
        migrations.AddField(
            model_name='contractors',
            name='sites',
            field=models.ManyToManyField(to='SM_app.Sites'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='sites',
            field=models.ManyToManyField(through='SM_app.SitesContacts', to='SM_app.Sites'),
        ),
    ]
