# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-09-21 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import pandas as pd
import os
from django.conf import settings

def load_initial(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    list_save = []
    item = apps.get_model('csvapp', 'item')
    csv_data = pd.read_csv(os.path.join(settings.BASE_DIR, 'Corpus.csv'))
    csv_dict = csv_data.to_dict('records')
    print csv_dict
    db_alias = schema_editor.connection.alias
    for data in csv_dict:
        item.objects.using(db_alias).bulk_create([item(key = data['key'], value = data['value'])])

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ('csvapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial),
    ]
