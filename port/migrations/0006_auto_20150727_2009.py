# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0005_auto_20150727_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planocliente',
            name='aviso_email',
            field=models.BooleanField(default=0, verbose_name='Aviso por email'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 20, 9, 36, 488972)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 20, 9, 36, 488972)),
        ),
    ]
