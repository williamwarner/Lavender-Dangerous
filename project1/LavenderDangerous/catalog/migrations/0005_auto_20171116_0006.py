# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 05:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20171115_2338'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requests',
            new_name='Request',
        ),
    ]
