# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 05:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='question_text',
            new_name='password',
        ),
        migrations.AddField(
            model_name='login',
            name='username',
            field=models.CharField(default=datetime.datetime(2016, 5, 22, 5, 27, 36, 18000, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
