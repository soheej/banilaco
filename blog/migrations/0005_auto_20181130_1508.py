# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-30 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181130_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='제품 유형', unique=True, verbose_name='제품 유형'),
        ),
    ]