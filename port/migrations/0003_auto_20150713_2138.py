# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_auto_20150710_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='cnpj',
            field=models.CharField(max_length=20, null=True, verbose_name='CNPJ', blank=True),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 21, 38, 20, 346878)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 21, 38, 20, 346878)),
        ),
    ]
