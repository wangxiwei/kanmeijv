# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0002_hdmovie'),
    ]

    operations = [
        migrations.CreateModel(
            name='HDTV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv_name', models.CharField(max_length=500)),
                ('tv_url', models.CharField(max_length=1000)),
                ('tv_download', models.CharField(max_length=2000)),
                ('tv_size', models.CharField(max_length=50)),
                ('tv_format', models.CharField(max_length=50)),
                ('tv_sub', models.CharField(max_length=2000)),
            ],
        ),
    ]