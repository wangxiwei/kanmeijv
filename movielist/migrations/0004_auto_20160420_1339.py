# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-20 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0003_auto_20160307_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLClicked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_clicked', models.CharField(max_length=100)),
                ('url_clicked', models.CharField(max_length=1000)),
                ('url_current', models.CharField(max_length=1000)),
                ('click_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='HDMovie',
        ),
    ]
