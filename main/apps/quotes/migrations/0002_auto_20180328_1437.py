# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaveQuotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=255)),
                ('quoteBy', models.CharField(max_length=255)),
                ('add_by', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('usersFave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='quotes.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotedBy', models.CharField(max_length=255)),
                ('quote', models.CharField(max_length=255)),
                ('addBy', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='stuff',
            name='add_by',
        ),
        migrations.DeleteModel(
            name='UserStuff',
        ),
        migrations.DeleteModel(
            name='Stuff',
        ),
    ]
