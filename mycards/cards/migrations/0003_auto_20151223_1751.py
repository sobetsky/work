# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 15:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20151222_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='date_issue',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 23, 17, 51, 46, 777733)),
        ),
        migrations.AlterField(
            model_name='cards',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cards',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.Profile'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='purchases',
            field=models.ManyToManyField(blank=True, null=True, to='cards.Purchases'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='date_of_approval',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 23, 17, 51, 46, 775264)),
        ),
    ]
