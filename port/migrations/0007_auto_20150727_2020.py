# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0006_auto_20150727_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 20, 20, 57, 789814)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='ddd',
            field=models.IntegerField(null=True, verbose_name='DDD', blank=True),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 20, 20, 57, 789814)),
        ),
    ]
