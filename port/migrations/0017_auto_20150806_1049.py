# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0016_auto_20150806_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cache',
            name='operadora',
        ),
        migrations.RemoveField(
            model_name='cache',
            name='tipo',
        ),
        migrations.AddField(
            model_name='cspretorno',
            name='operadora',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='cspretorno',
            name='tipo',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 6, 10, 49, 26, 435204)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 5, 10, 49, 26, 435204)),
        ),
    ]
