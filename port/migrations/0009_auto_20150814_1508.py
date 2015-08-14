# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0008_auto_20150814_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='cod_revenda',
            field=models.CharField(default=0, unique=True, max_length=100, verbose_name='Codigo da Revenda'),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 14, 15, 8, 5, 891071)),
        ),
        migrations.AlterField(
            model_name='planocliente',
            name='expira_em',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 13, 15, 8, 5, 891071)),
        ),
    ]
