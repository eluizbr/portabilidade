# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0009_auto_20150728_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 12, 17, 55, 175447)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 12, 17, 55, 175447)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='saldo_baixo',
            field=models.CharField(default=0, max_length=5, verbose_name='Saldo baixo'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='sem_saldo',
            field=models.CharField(default=0, max_length=5, verbose_name='Sem saldo'),
        ),
    ]
