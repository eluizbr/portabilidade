# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revenda',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='revenda',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 17, 12, 43, 31, 789425), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='revenda',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 17, 12, 43, 37, 149399), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='revenda',
            name='nome_fantasia',
            field=models.CharField(max_length=100, verbose_name='Nome fantasia'),
        ),
    ]
