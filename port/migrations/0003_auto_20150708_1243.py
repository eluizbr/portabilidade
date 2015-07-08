# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_auto_20150708_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='planocliente',
            name='cache',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='planocliente',
            name='tempo',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 12, 43, 14, 61401)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 43, 14, 61401)),
        ),
    ]
