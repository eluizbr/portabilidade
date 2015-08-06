# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0015_auto_20150806_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='cache',
            name='operadora',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='cache',
            name='tipo',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 6, 10, 48, 50, 624680)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 5, 10, 48, 50, 624680)),
        ),
    ]
