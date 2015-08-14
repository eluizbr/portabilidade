# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0012_auto_20150814_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='cod_revenda',
            field=models.CharField(default=0, max_length=100, verbose_name='Codigo da Revenda'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 14, 15, 35, 38, 71194)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 13, 15, 35, 38, 71194)),
        ),
    ]
