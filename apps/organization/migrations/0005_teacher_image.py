# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-18 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('organization', '0004_auto_20170417_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teachers/%y/%m', verbose_name='\u5934\u50cf'),
        ),
    ]