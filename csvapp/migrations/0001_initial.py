# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-09-21 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('key', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
            ],
        ),
    ]