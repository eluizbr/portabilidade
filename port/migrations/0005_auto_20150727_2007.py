# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0004_auto_20150713_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='planocliente',
            name='aviso_email',
            field=models.BooleanField(default=b'None', verbose_name='Aviso por email'),
        ),
        migrations.AddField(
            model_name='planocliente',
            name='ddd',
            field=models.IntegerField(default=31, verbose_name='DDD'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 20, 7, 19, 494084)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 20, 7, 19, 494084)),
        ),
    ]
