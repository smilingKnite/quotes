# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20180328_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favequotes',
            name='usersFave',
        ),
        migrations.AddField(
            model_name='users',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Birth'),
        ),
    ]
