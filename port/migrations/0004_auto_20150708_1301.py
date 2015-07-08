# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0003_auto_20150708_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planocliente',
            name='cache',
            field=models.CharField(default=0, max_length=1, verbose_name='Cache habilitado', choices=[(b'0', b'Desativado'), (b'1', b'Ativado')]),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 8, 13, 1, 53, 778711)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 13, 1, 53, 778711)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='tempo',
            field=models.IntegerField(default=60, verbose_name='Tempo do cache em minutos'),
        ),
    ]
