# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birthday',
            field=models.DateField(blank=True, default=b'27/06/1999'),
        ),
    ]