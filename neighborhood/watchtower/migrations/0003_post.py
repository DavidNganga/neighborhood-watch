# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchtower', '0002_neighborhood_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.TextField(max_length=50)),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_parastatal', to='watchtower.Neighborhood')),
            ],
        ),
    ]