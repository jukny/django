# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 19:19
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='collection',
            managers=[
                ('create_collection', django.db.models.manager.Manager()),
            ],
        ),
    ]