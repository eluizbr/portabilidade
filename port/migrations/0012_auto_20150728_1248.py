# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0011_auto_20150728_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 12, 48, 17, 99745)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 12, 48, 17, 99745)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='saldo_baixo',
            field=models.BooleanField(default=0, verbose_name='Saldo baixo'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='sem_saldo',
            field=models.BooleanField(default=0, verbose_name='Sem saldo'),
        ),
    ]
