# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0025_auto_20150811_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='plano',
            name='especial',
            field=models.CharField(default=0, max_length=200, choices=[(b'0', b'Ilimitado'), (b'1', b'normal')]),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 11, 10, 55, 37, 867714)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 10, 55, 37, 867714)),
        ),
    ]
