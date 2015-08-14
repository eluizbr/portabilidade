# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0005_auto_20150814_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='cod_cliente',
            field=models.CharField(unique=True, max_length=100, verbose_name='Codigo do Cliente'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 14, 14, 11, 28, 419470)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 13, 14, 11, 28, 419470)),
        ),
    ]
