# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-26 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchtower', '0010_auto_20180526_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighborhood',
            old_name='event',
            new_name='event_details',
        ),
    ]
