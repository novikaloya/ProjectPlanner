# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-28 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planner', '0002_auto_20190527_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_img'),
        ),
    ]
