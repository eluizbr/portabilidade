# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0007_auto_20150727_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='planocliente',
            name='retorno',
            field=models.CharField(default=1, max_length=5, verbose_name='Retorno', choices=[(b'1', b'CSP Completo'), (b'2', b'C\xc3\xb3digo de operadora apenas')]),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 20, 58, 50, 257370)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 20, 58, 50, 257370)),
        ),
    ]
