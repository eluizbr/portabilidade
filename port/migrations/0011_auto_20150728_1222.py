# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0010_auto_20150728_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 12, 22, 41, 69767)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 12, 22, 41, 69767)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='saldo_baixo',
            field=models.CharField(default=0, max_length=5, null=True, verbose_name='Saldo baixo', blank=True),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='sem_saldo',
            field=models.CharField(default=0, max_length=5, null=True, verbose_name='Sem saldo', blank=True),
        ),
    ]
