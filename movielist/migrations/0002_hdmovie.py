# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HDMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HD_name', models.CharField(max_length=500)),
                ('HD_url', models.CharField(max_length=1000)),
                ('HD_size', models.CharField(max_length=50)),
                ('HD_sbu', models.CharField(max_length=1000)),
            ],
        ),
    ]
