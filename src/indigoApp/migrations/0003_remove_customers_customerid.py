# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 05:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indigoApp', '0002_auto_20160220_0442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='CustomerId',
        ),
    ]
